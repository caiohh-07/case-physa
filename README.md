# 🐍 Cobras e Escadas – Simulador com Múltiplos Modos de Jogo

## 1. 🎯 Visão Geral do Projeto

Este projeto implementa uma simulação do clássico jogo **Cobras e Escadas**, com suporte para múltiplas regras de jogo (modos). Ele permite:

- Simular diversas partidas entre jogadores.
- Variar regras como escadas com chance, imunidade a cobras e posições iniciais.
- Gerar histórico completo de cada simulação.
- Realizar análises estatísticas sobre os resultados.

O projeto segue princípios de engenharia de software: modularização, separação de responsabilidades e suporte a testes e extensões.

---

## 2. ▶️ Executar o jogo
```bash
python run_game.py

---

## 3. ⚙️ Como Rodar o projeto

### ✅ Requisitos

- **Python**: versão 3.11.5
- Instalar bibliotecas necessárias:

```bash
pip install -r requirements.txt

---

## 4. 🗂️ Estrutura de pastas do projeto

.
├── config/
│   └── tabuleiro.json          # Configurações do tabuleiro: tamanho, escadas e cobras
│
├── core/
│   ├── board.py                # Classe Board: lógica do tabuleiro
│   ├── player.py               # Classe Player: estado e movimentação dos jogadores
│   ├── game_base.py            # Classe base do jogo (turnos, lógica comum)
│   ├── utils.py                # Funções auxiliares (rolar dado, etc.)
│   └── __init__.py
│
├── modes/
│   ├── game_standard.py              # Modo 1: Jogo padrão
│   ├── game_conditional_climb.py     # Modo 2: Escada com 50% de chance de subit
│   ├── game_variable_start.py        # Modo 3: Variação da posição inicial do jogador 2
│   ├── game_immune_first_snake.py    # Modo 4: Imunidade à primeira cobra do jogador 2
│   └── __init__.py
│
├── run_game.py       # Arquivo principal para executar as simulações
|         
└── README.md         # Este arquivo

---

## 5. 🧱 Explicação das Classes

### `Board` (em `core/board.py`)
Responsável por representar o tabuleiro:
- Carrega o JSON com tamanho, cobras e escadas.
- Aplica as transições de casa (ex: subir uma escada, descer por uma cobra).
- Informa se uma posição tem escada ou cobra.

### `Player` (em `core/player.py`)
Modela os jogadores:
- Armazena nome e posição atual.
- Permite movimentação com `mover_para()`.

### `GameBase` (em `core/game_base.py`)
Contém a lógica comum a todos os modos de jogo:
- Gerencia os turnos, rodada, jogadores e histórico.
- Executa a lógica de movimentação e verificação de vitória.

### `GameStandard` (em `modes/game_standard.py`)
Modo padrão de jogo, sem regras especiais.

### `GameCoditionalClimb` (em `modes/game_conditional_climb.py`)
Escadas só funcionam com 50% de chance.

### `GameImmuneFirstSnake` (em `modes/game_immune_first_snake.py`)
Cada jogador ignora a **primeira cobra** em que cair.

### `GameVariableStart` (em `modes/game_variable_start.py`)
Executa jogos simulando diferentes **posições iniciais do Jogador 2**.

### `utils.py`
Contém utilitários como:
- `rolar_dado()`: simula o lançamento de um dado.
- Outras funções auxiliares para manipulação e análise dos dados.


