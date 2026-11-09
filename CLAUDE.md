# Ciência de Dados: material da disciplina

Site Quarto com os roteiros das aulas (`aulas/NN-*.qmd`), em português brasileiro, publicado pelo workflow em `.github/workflows/publish.yml`. Cada aula nova também entra na `sidebar` do `_quarto.yml` e na lista do `index.qmd`, com uma descrição de uma linha.

## Roteiros de aula

- Os roteiros executam Python (`jupyter: kernel: python3`) e usam `freeze`: depois de editar, renderize com `quarto render aulas/<arquivo>.qmd` a partir da raiz e versione também `_freeze/aulas/<arquivo>/`. Apague figuras antigas do `_freeze` que o resultado não usa mais.
- As bases ficam em `aulas/<base>/data/` e são lidas com caminhos relativos à pasta `aulas/`.
- Estrutura padrão: Motivação (com pergunta-guia), Objetivos de aprendizagem, callout "Como usar este roteiro", seções numeradas, Síntese, Perguntas para consolidar (respostas em callouts recolhidos "Como pensar sobre isso"), Para casa (o último item é "Restart Kernel and Run All") e Referências.
- Todo número citado no texto deve conferir com a saída renderizada.

## Estilo de código

- Comentário-título em português no início de cada célula; nomes de variáveis em inglês; anotações `# <n>` explicadas logo abaixo da célula.
- pandas em *method chaining* entre parênteses, um método por linha, sem mutação in-place nem `\` para continuar linhas.
- Só crie funções com reuso real (duas ou mais chamadas, laço sobre parâmetros ou redução grande de código); definição e uso na mesma célula.
- Nas aulas de aprendizado de máquina, coeficientes, métricas e modelos de referência vêm do scikit-learn (`LinearRegression`, `sklearn.metrics`, `DummyRegressor`, `cross_validate`…). Fórmulas aparecem só no texto, não como cálculo manual paralelo.
- Paleta dos gráficos: `#1F4E79`, `#A1C9F4`, `#DD8452`, `#DDDDDD`, `#333333`, sempre escrita como literal em cada chamada, sem constantes de cor. O mesmo vale para as sementes (`random_state=42`): nada de constantes como `SEED`.
- Toda tabela vai para uma variável com nome descritivo e é exibida na última linha da célula; nada de `pd.DataFrame(...)` solto.
- Células curtas, com uma etapa cada (cálculo, tabela ou gráfico): cerca de 15 linhas de código, ou 25 em gráficos.
- Para refatorar o código de um roteiro, use a skill `/refatorar-codigo`, definida em `.claude/skills/refatorar-codigo/SKILL.md`.

## Estilo de texto

- Fora da Motivação e da Recapitulação, evite autorreferências ("da Aula 6", "seção 4.1"); cite o conceito pelo nome.
- Vírgula decimal no texto ($0{,}48$) e ponto no código.
- Para revisar textos (coesão e coerência, norma culta e humanização), use a skill `/revisar-texto`, definida em `.claude/skills/revisar-texto/SKILL.md`.
