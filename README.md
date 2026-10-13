# Gerenciador de Campeonato de Pontos Corridos

**Disciplina:** Paradigmas de Programação — UNAMA
**Professor:** Rodrigo Medeiros Costa
**Linguagem:** Python 3
**Paradigma:** Imperativo

## Integrantes

| Nome | GitHub | Matrícula |
|------|--------|--------------|
| Orlando de Araújo Gonçalves | @oLanxs | 04161229

## Vídeo de demonstração

https://drive.google.com/drive/folders/1LvD9QHcx0LkX7vID3bKuZZR8OaHwfn4C?usp=share_link

## 1. Descrição do problema

Organizar um campeonato de pontos corridos exige atualizar a tabela de
classificação a cada jogo. O programa automatiza isso: cadastra os times,
registra resultados e mostra a classificação ordenada.

**Entradas:** nome dos times; para cada partida, mandante, visitante e gols de cada um.

**Regras principais:**
- Vitória = 3 pontos; empate = 1 ponto; derrota = 0.
- Critérios de desempate, nesta ordem: pontos, vitórias, saldo de gols, gols pró.
- Não é permitido cadastrar times repetidos, um time jogar contra si mesmo ou repetir o mesmo confronto (mandante x visitante).
- Gols devem ser números inteiros maiores ou iguais a zero.

**Resultados esperados:** tabela com posição, pontos, jogos, vitórias, empates, derrotas, gols pró, gols contra e saldo; lista das partidas; destaque do líder.

## 2. Instruções de execução

**Requisito:** Python 3.8 ou superior.

```bash
git clone <link-do-repositorio>
cd <pasta-do-repositorio>
python campeonato.py
```

Dica: a opção **5** do menu carrega dados de exemplo para testar rapidamente.

## 3. Explicação da solução

O estado do programa fica em duas listas globais, `times` e `partidas`. Cada
operação do menu altera esse estado passo a passo.

| Elemento imperativo | Onde aparece no código |
|---------------------|------------------------|
| **Sequência de instruções** | `registrar_partida()` executa em ordem: validar times, ler gols, guardar a partida, atualizar os dois times |
| **Variáveis e atribuições (mudança de estado)** | `atualizar_estatisticas()` altera `pontos`, `jogos`, `gols_pro` etc. com `+=`; `partidas.append(...)` e `times.append(...)` alteram as listas |
| **Decisões** | `if/elif/else` em `atualizar_estatisticas()` (vitória, empate ou derrota), nas validações de `registrar_partida()` e no menu de `main()` |
| **Repetições** | `while` em `ler_inteiro()` e em `main()` (laço do menu); `for` em `buscar_time()`, `exibir_classificacao()` e no Bubble Sort |
| **Funções/procedimentos** | `cadastrar_time()`, `registrar_partida()`, `ordenar_tabela()`, `exibir_classificacao()`, entre outras |

**Exemplo de mudança de estado:** ao registrar Paysandu 2 x 1 Remo, o time
Paysandu passa de `pontos=0, vitorias=0` para `pontos=3, vitorias=1`, e o Remo
passa de `derrotas=0` para `derrotas=1`.

**Ordenação:** `ordenar_tabela()` usa Bubble Sort sobre uma cópia da lista,
comparando os times pela função `criterio()`. A cópia preserva a ordem original de cadastro.

## 4. Reflexão sobre o desenvolvimento

•⁠  ⁠*Decisões:* usei listas de dicionários para guardar os dados de cada time e separei o código em funções pequenas, cada uma com uma tarefa. Implementei o Bubble Sort manualmente em vez de ⁠ sorted() ⁠ para evidenciar repetições e trocas de variáveis.
•⁠  ⁠*Dificuldades:* definir os critérios de desempate e validar as entradas do usuário (números inválidos, nomes repetidos, partida duplicada).
•⁠  ⁠*Melhorias possíveis:* salvar os dados em arquivo para não perdê-los ao fechar, permitir editar ou remover uma partida, gerar o calendário automaticamente e incluir jogos de returno
