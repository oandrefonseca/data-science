---
name: revisar-texto
description: Revisa textos em português brasileiro em três passadas (coesão e coerência, norma culta e humanização), preservando fatos, números e código. Use quando o usuário pedir para revisar, corrigir, melhorar o ritmo ou "humanizar" um roteiro de aula (.qmd) ou qualquer outro texto do projeto.
argument-hint: "[arquivo] [coesao|norma|humanizacao|tudo]"
---

# Revisão de texto em PT-BR

Revise o texto indicado pelo usuário: um arquivo (por padrão, o roteiro aberto no editor) ou um texto colado na conversa. O segundo argumento escolhe as passadas; sem ele, faça as três, na ordem abaixo.

## Regras que valem para todas as passadas

- **Não invente nem altere fatos.** Números, nomes, resultados e afirmações técnicas permanecem como estão. Se uma afirmação não tiver respaldo no próprio texto ou nos dados, não a reforce: atenue-a ("uma explicação possível é…") e mencione isso ao usuário.
- **Não toque em código.** Em arquivos `.qmd`, as células ```` ```{python} ```` e ```` ```{r} ````, as fórmulas em LaTeX, os nomes entre crases e o YAML do cabeçalho ficam idênticos. Antes de sobrescrever um roteiro, salve uma cópia no scratchpad e, ao final, confira que as células de código são iguais às da cópia.
- **Mantenha a estrutura do roteiro.** Seções e subseções numeradas, "Objetivos de aprendizagem", "Síntese", "Perguntas para consolidar", "Para casa", "Referências", os callouts e as anotações numeradas de código (`# <1>` e a lista abaixo da célula) fazem parte do modelo das aulas e não devem ser removidos, salvo pedido explícito.
- **Evite autorreferências.** Fora da Motivação e da Recapitulação, não aponte de onde vem cada conceito ("da Aula 6", "como na seção 4.1"). Cite o conceito pelo nome ("o exemplo dos polinômios", "o modelo de referência").
- **Confira depois de editar.** Se o arquivo for um roteiro, renderize com `quarto render aulas/<arquivo>.qmd` (a partir da raiz do projeto) e confirme que não há erros nem avisos.

## Passada 1: coesão e coerência

Atue como um revisor especializado, sem reescrever o que já funciona.

- Corrija referências sem antecedente ("essa regra", "como vimos") e conectivos que não ligam as ideias que conectam.
- Verifique se cada afirmação bate com o que o texto mostra: contagens ("três observações" seguidas de duas), leituras de gráficos e tabelas, números citados versus números calculados.
- Elimine contradições, tautologias e frases que só fazem sentido com um contexto que foi removido.
- Melhore o ritmo para o público-alvo (alunos de graduação): divida frases longas demais, retire repetições de palavras próximas e redundâncias.

## Passada 2: norma culta

Atue como um revisor profissional de PT-BR e faça apenas as correções necessárias, mantendo o tom, a voz e a intenção do autor.

- Ortografia, gramática normativa, concordância verbal e nominal, regência, pontuação e crase.
- Atenção a casos frequentes: regência de "aumentar em", "diminuir em"; "da mesma" (e não "de mesma"); vírgulas em torno de "por exemplo" e de orações intercaladas; dois-pontos antes de explicações; verbo ausente em comparações ("quanto maior…, mais… fica").
- Construções aceitas pela norma e coerentes com o tom (como "o quanto") não precisam ser trocadas.

## Passada 3: humanização

Atue como editor especialista em humanização de conteúdo e remova padrões típicos de texto gerado por IA, mantendo todas as informações intactas.

- **Formatação:** troque listas de tópicos com rótulo em negrito ("- **Assimetria.** …") por parágrafos corridos, sempre que a lista não for um passo a passo, uma enumeração real ou parte do modelo do roteiro. Mantenha o negrito apenas na primeira definição de um termo técnico. Tabelas que organizam dados continuam como tabelas.
- **Fórmulas prontas:** elimine aberturas e fechamentos previsíveis ("Vamos ler os números:", "Três observações:", "A lição é direta:", "O ponto mais importante é…", "E há uma surpresa:") e callouts que só repetem uma frase do texto.
- **Vocabulário de IA:** evite "com certeza", "em resumo", "vale ressaltar", "além disso", "fundamental", "crucial", "jornada", "desmistificar", "de quebra", "literalmente", "elegante", "enorme" e similares.
- **Cadência:** alterne períodos curtos e longos, prefira a voz ativa e um tom de conversa com o aluno, sem perder a precisão.
- Ao terminar, rode uma busca pelos termos da lista acima para confirmar que nenhum sobrou.

## Entrega

- Se o pedido for só a humanização e o usuário pedir "apenas o texto final", entregue apenas isso: em arquivo, o caminho do arquivo revisado (e da cópia de segurança); em texto colado, o texto revisado, sem preâmbulo.
- Nos demais casos, liste as correções de forma breve, agrupadas por tipo (coesão, coerência, norma, ritmo), com o trecho antes e depois quando ajudar.
