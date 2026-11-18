"""Gera os arquivos de tcga-brca/data/ a partir do TCGA-BRCA (GDC, via UCSC Xena).

Não faz parte do roteiro: roda uma única vez, baixa ~350 MB e leva alguns minutos.
Execute a partir da pasta aulas/:  python tcga-brca/preparar_dados.py

Entradas (GDC Xena Hub e TCGA Xena Hub):
- TCGA-BRCA.star_tpm.tsv.gz: expressão em log2(TPM + 1), genes Ensembl x amostras.
- gencode.v36.annotation.gtf.gene.probemap: Ensembl -> símbolo do gene.
- BRCA_clinicalMatrix: anotação clínica, de onde vem o subtipo PAM50 (PAM50Call_RNAseq).

Saídas:
- brca_hvgs_log2.parquet: 1.095 pacientes x 505 genes (500 mais variáveis + marcadores do dicionário).
- dicionario_marcadores.json: 5 perfis moleculares com 2 a 4 genes cada.
- brca_pam50.csv: subtipo PAM50 oficial, usado só como validação externa no fim da aula.
"""

import json
from pathlib import Path

import pandas as pd

TPM_URL = "https://gdc-hub.s3.us-east-1.amazonaws.com/download/TCGA-BRCA.star_tpm.tsv.gz"
PROBEMAP_URL = "https://gdc-hub.s3.us-east-1.amazonaws.com/download/gencode.v36.annotation.gtf.gene.probemap"
CLINICAL_URL = "https://tcga-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA.BRCA.sampleMap%2FBRCA_clinicalMatrix"

OUT = Path("tcga-brca/data")
N_HVG = 500
MARKERS = {
    "Hormonal": ["ESR1", "PGR", "GATA3", "FOXA1"],
    "HER2": ["ERBB2", "GRB7"],
    "Basal": ["KRT5", "KRT16", "FOXC1", "EGFR"],
    "Proliferativo": ["MKI67", "AURKA"],
    "Estromal": ["COL14A1", "C7", "ADH1B"],
}

# Expressão (já em log2(TPM + 1)) e mapa Ensembl -> símbolo
tpm = pd.read_csv(TPM_URL, sep="\t", index_col=0)
symbols = pd.read_csv(PROBEMAP_URL, sep="\t", index_col=0)["gene"]

# Apenas tumores primários (código de amostra 01), uma alíquota por paciente
primary = sorted(c for c in tpm.columns if c[13:15] == "01")
patients = pd.Series(primary, index=primary).str[:12]
primary = patients[~patients.duplicated()].index

expr = tpm[primary].set_axis([c[:12] for c in primary], axis=1)
expr.index = symbols.reindex(expr.index).values
expr = expr.loc[expr.index.notna() & ~expr.index.duplicated()]

# Remove imunoglobulinas, receptores de células T, lncRNAs sem nome e genes pouco expressos
noise = r"^(IG[HKL][VCJDG]|IGH[AGEMD]|IGLL|JCHAIN|TR[ABGD][VCJ]|A[A-Z]\d{6}\.\d|Z\d{5}|MIR|SNOR|LINC|MT-|RPL|RPS|ENSG|.*-AS\d)"
expr = expr.loc[~expr.index.str.match(noise) & ~expr.index.str.contains(r"\.")]
expr = expr.loc[expr.mean(axis=1) >= 1].T

# 500 genes de maior variância (HVGs) + marcadores do dicionário que ficaram de fora
marker_genes = [g for genes in MARKERS.values() for g in genes]
hvgs = expr.var().sort_values(ascending=False).index[:N_HVG].tolist()
genes = hvgs + [g for g in marker_genes if g not in hvgs]

OUT.mkdir(parents=True, exist_ok=True)
expr[genes].round(3).rename_axis("paciente").to_parquet(OUT / "brca_hvgs_log2.parquet")
(OUT / "dicionario_marcadores.json").write_text(json.dumps(MARKERS, ensure_ascii=False, indent=2))

# Subtipo PAM50 oficial, alinhado aos mesmos pacientes
clinical = pd.read_csv(CLINICAL_URL, sep="\t", index_col=0)
pam50 = clinical["PAM50Call_RNAseq"].rename(index=lambda s: s[:12])
pam50 = pam50[~pam50.index.duplicated()]
(
    pam50.reindex(expr.index)
    .rename("pam50")
    .rename_axis("paciente")
    .reset_index()
    .to_csv(OUT / "brca_pam50.csv", index=False)
)
