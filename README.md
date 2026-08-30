# Ciência de Dados

Site Quarto com o material da disciplina de Ciência de Dados: roteiros práticos de aula e o enunciado do trabalho final.

## Estrutura

```
.
├── _quarto.yml          # configuracao do site (tema, navegacao)
├── index.qmd             # pagina inicial
└── aulas/
    ├── roteiro-aula1-ferramentas-ambiente-versionamento.qmd
    ├── roteiro-aula2-introducao-dados-tabulares.qmd
    └── trabalho-final-analise-vendas.qmd
```

O `projeto-vendas/`, criado pelos alunos ao longo dos roteiros, é um projeto à parte (repositório próprio) e não faz parte deste site.

## Rodando localmente

```bash
quarto preview
```

## Publicação

O site é publicado no GitHub Pages a cada push na branch `main`, via o workflow em [.github/workflows/publish.yml](.github/workflows/publish.yml). Em **Settings > Pages**, a *source* do repositório deve estar configurada como **GitHub Actions**.
