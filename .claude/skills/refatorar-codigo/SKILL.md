---
name: refatorar-codigo
description: Refatora as células de código dos roteiros (.qmd) com princípios de clean code, encadeamento de métodos no pandas entre parênteses, células curtas e tabelas sempre atribuídas a variáveis, sem alterar nenhum resultado. Use quando o usuário pedir para refatorar, limpar, simplificar ou melhorar a legibilidade do código de uma aula.
argument-hint: "[arquivo] [seção opcional]"
---

# Refatoração do código dos roteiros

Refatore as células ```` ```{python} ```` do roteiro indicado (por padrão, o arquivo aberto no editor; se o usuário citar uma seção, limite-se a ela). O objetivo é um código que o aluno leia de cima para baixo e entenda sem esforço, com o mesmo resultado de antes.

## Regra inviolável: os resultados não mudam

Refatorar é mudar a forma, nunca o resultado. Toda tabela, todo número impresso e toda figura devem sair iguais. O procedimento do final desta skill verifica isso; se algo mudar, desfaça a alteração responsável.

## 1. Encadeamento de métodos no pandas

Toda transformação com dois ou mais métodos fica dentro de parênteses, com o objeto de partida sozinho na primeira linha e um método por linha:

```python
coef_range = (
    pd.DataFrame(fold_coefs)
    .groupby("base")[["beta_0", "beta_1"]]
    .agg(["min", "max"])
    .round(4)
)
```

- Nunca use `\` para continuar linhas.
- Sem mutação in-place: nada de `df["col"] = ...`, `.loc[...] = ...` ou `inplace=True`. Crie colunas com `.assign(col=lambda df: ...)`; para nomes com espaço, `.assign(**{"nome com espaço": ...})`.
- Prefira `.query`, `.rename`, `.pipe`, `.loc[lambda df: ...]` dentro da cadeia a variáveis intermediárias descartáveis.
- Chamadas de um único método (`x.mean()`, `df.head()`) e código NumPy, scikit-learn ou Matplotlib podem ficar em uma linha.
- Anote com `# <n>` o primeiro uso de `.assign`, `lambda`, `.pipe` ou `.query` no roteiro.

## 2. Tabelas sempre atribuídas

Nenhum `pd.DataFrame(...)`, `.agg(...)` ou `.describe()` fica "solto" como expressão. O resultado vai para uma variável com nome descritivo, e a célula termina exibindo essa variável na última linha:

```python
metrics = pd.DataFrame(...).T.round(4)

metrics
```

A exceção é a inspeção direta de uma variável que já existe (`housing.head()`, `housing.describe()`), que pode continuar como última linha da célula.

## 3. Células curtas, uma etapa por célula

- Uma célula faz uma coisa: calcular, montar uma tabela ou desenhar um gráfico. Se ela faz duas, divida-a.
- O limite é de cerca de 15 linhas de código, sem contar comentários e linhas em branco. Células de gráfico, com muitas linhas de formatação, podem chegar a cerca de 25.
- Cada célula começa com uma linha em branco e um comentário-título em português que diz o que ela faz. Ao dividir uma célula, escreva um título para cada parte.
- Células ocultas (`#| echo: false`) seguem as mesmas regras.

## 4. Clean code

- **Nomes que explicam.** Variáveis em inglês, descritivas e no padrão `snake_case`. As abreviações aceitas são as convenções da área (`X`, `y`, `X_dev`, `fig`, `ax`, `df` dentro de `lambda`) e índices curtos em compreensões. Não reaproveite um nome para outro tipo de objeto (por exemplo, `grid` como DataFrame em uma célula e como array em outra) nem use nomes que escondem funções ou módulos (`fit`, `sum`, `list`, `stats`).
- **Uma responsabilidade por bloco.** Separe o cálculo da apresentação. Evite laços com `append` quando uma compreensão de lista ou de dicionário for mais clara.
- **Sem repetição.** Estruturas reutilizadas em várias células, como listas de colunas (`features_m2`), ficam em uma variável definida uma vez. Cores e sementes aleatórias são exceção: ficam como valores literais em cada chamada (`color="#1F4E79"`, `random_state=42`), mesmo que se repitam, para que cada célula possa ser lida sozinha. Não crie constantes como `SEED` ou `DARK_BLUE`. Crie funções apenas com reuso real: chamadas em dois ou mais lugares, aplicadas em laço sobre parâmetros ou substituindo um bloco repetido de cerca de 10 linhas, com definição e primeiro uso na mesma célula.
- **Pouco aninhamento.** No máximo dois níveis de laço ou condição. Se passar disso, reorganize.
- **Sem código morto.** Remova imports, variáveis, argumentos e linhas que não afetam o resultado.
- **Comentários que explicam o porquê.** O comentário-título diz o que a célula faz. As anotações `# <n>` explicam a parte não óbvia. Não comente o que o código já diz.
- **Bibliotecas, não contas à mão.** Nas aulas de aprendizado de máquina, coeficientes, métricas e modelos de referência vêm do scikit-learn, não de fórmulas reimplementadas.
- **Formato.** Siga o PEP 8, com linhas de até cerca de 90 caracteres e quebras alinhadas dentro dos parênteses.
- **Imports.** Ficam todos na primeira célula, agrupados por biblioteca (bibliotecas-base, matplotlib, scipy, sklearn) e em ordem alfabética dentro de cada grupo, com linhas de até 79 caracteres. Quando um `from ... import` tiver vários nomes, abra parênteses e ponha um nome por linha, com vírgula final:

  ```python
  from sklearn.metrics import (
      mean_absolute_error,
      r2_score,
  )
  ```

## Procedimento

1. **Cópia de segurança.** Salve uma cópia do `.qmd` no scratchpad e extraia as saídas atuais de `_freeze/aulas/<arquivo>/execute-results/html.json`: os blocos `cell-output` de texto e a quantidade de figuras.
2. **Refatoração.** Aplique as regras acima célula a célula. Ao dividir ou reorganizar células, atualize as anotações `# <n>` e a lista explicativa abaixo de cada célula, além de qualquer frase do texto que descreva o código.
3. **Renderização.** Rode `quarto render aulas/<arquivo>.qmd` a partir da raiz do projeto e confirme que não há erros nem avisos.
4. **Comparação.** Compare as saídas de texto novas com as antigas. Ignore apenas a numeração das células e diferenças de HTML que não mudam valores. Os números devem ser idênticos, e a quantidade de figuras, a mesma. Abra as figuras das células alteradas para conferir.
5. **Limpeza.** Apague do `_freeze` as figuras que o resultado novo não usa mais.
6. **Relatório.** Liste o que mudou, agrupado por regra (encadeamento, tabelas atribuídas, divisão de células, nomes, código morto), e informe o caminho da cópia de segurança.
