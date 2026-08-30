# Ciência de Dados

Site Quarto com o material da disciplina de Ciência de Dados: roteiros práticos de aula e o enunciado do trabalho final.

## Estrutura

```
.
├── _quarto.yml          # configuracao do site (sidebar, tema, execucao)
├── styles.css            # customizacoes de CSS
├── index.qmd             # pagina inicial
└── aulas/
    ├── roteiro-aula1-ferramentas-ambiente-versionamento.qmd
    ├── roteiro-aula2-introducao-dados-tabulares.qmd
    └── trabalho-final-analise-vendas.qmd
```

Os projetos criados pelos alunos ao longo dos roteiros (como o `projeto-vendas`) ficam em `projetos/`, cada um com repositório próprio, e não fazem parte deste site.

## Rodando localmente

```bash
quarto preview
```

## Publicação

O site é publicado no GitHub Pages a cada push na branch `main`, via o workflow em [.github/workflows/publish.yml](.github/workflows/publish.yml). Em **Settings > Pages**, a *source* do repositório deve estar configurada como **GitHub Actions**.
