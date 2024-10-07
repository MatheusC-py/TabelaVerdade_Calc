# TabelaVerdade_Calc

## Descrição

O **TabelaVerdade_Calc** é uma ferramenta desenvolvida em Python para criar tabelas verdade a partir de expressões lógicas fornecidas pelo usuário. O programa suporta diversas operações lógicas, como AND, OR, NOT e XOR, e gera automaticamente a tabela verdade completa, permitindo uma análise detalhada dos resultados para cada combinação de variáveis.

## Funcionalidades

- **Operações Lógicas Suportadas**:
  - `AND` (representado por `*` ou `.`)
  - `OR` (representado por `+`)
  - `NOT` (representado por `!`)
  - `XOR` (representado por `!=`)
- **Entrada Personalizada**: O usuário pode inserir qualquer expressão lógica usando as operações mencionadas.
- **Geração Automática de Tabelas Verdade**: O programa cria a tabela verdade completa para qualquer expressão fornecida, com base nas variáveis envolvidas.
- **Saída Organizada**: A tabela verdade é exibida de forma clara e formatada diretamente no terminal.

## Exemplo de Uso

### Expressões Suportadas:

1. `A * B + !C` (equivalente a: `A AND B OR NOT C`)
2. `A != B` (equivalente a: `A XOR B`)

## Requisitos:

1. Python 3.x
2. Biblioteca Os (apenas para realizar limpeza de terminal)
