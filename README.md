# 🎲 Simulador de Cobras e Escadas com Múltiplos Modos de Jogo

Este projeto simula o jogo clássico **Cobras e Escadas** com variações de regras para análise estatística de desempenho dos jogadores. É possível executar partidas individuais, simulações em massa e analisar os eventos ocorridos durante o jogo com base em diferentes modos de jogo.

---

## 🚀 Objetivos

- Simular milhares de jogos com regras personalizadas.
- Avaliar se o jogador que começa tem vantagem estatística.
- Registrar eventos de cada turno e salvar o histórico.
- Exportar dados em formato `.parquet` para análise posterior com pandas.

---

## 📦 Estrutura do Projeto
snake_ladders_sim/
├── config/
│ └── tabuleiro.json
├── core/
│ ├── board.py
│ ├── player.py
│ ├── game_base.py
│ ├── utils.py
│ └── init.py
├── modes/
│ ├── game_standard.py
│ ├── game_uncertain_climb.py
│ ├── game_variable_start.py
│ └── game_immune_first_snake.py
├── simulations/
│ ├── run_game.py
│ ├── play_game_standard.py
│ ├── play_game_uncertain_climb.py
│ └── play_game_immune_first_snake.py
├── tests/
│ └── test_game_standard.py
└── README.md


---

## 🎮 Modos de Jogo Disponíveis

| Modo | Classe                          | Descrição                                                                 |
|------|----------------------------------|---------------------------------------------------------------------------|
| 1    | `GameStandard`                  | Jogo tradicional, sem regras extras                                       |
| 2    | `GameUncertainClimb`           | Jogadores têm 50% de chance de subir escadas                             |
| 3    | `GameVariableStart`            | Jogador 2 começa em várias posições e simula várias partidas por posição |
| 4    | `GameImmuneFirstSnake`         | Jogadores ignoram a primeira cobra que encontrarem                       |

---

## 🛠️ Requisitos (Instale manualmente)

Instale os seguintes pacotes com `pip install`:

- `pandas`
- `numpy`
- `scipy`
- `pyarrow`
- (opcional) `matplotlib` e `seaborn` para gráficos
- (opcional) `pytest` para rodar os testes

---

## ▶️ Como Executar

### Jogar uma partida padrão:
```bash
python simulations/play_game_standard.py


