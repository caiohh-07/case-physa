from core.game_base import GameBase
from core.board import Board

class GameVariableStart:
    def __init__(self, board: Board, posicao_inicial_jogador2: int):
        self.board = board
        self.posicao = posicao_inicial_jogador2
        self.resultados = []

    def jogar(self):
        jogo = GameBase(self.board)
        jogo.jogadores[0].mover_para(1)
        jogo.jogadores[1].mover_para(self.posicao)

        vencedor = jogo.jogar()

        self.resultados.append({
            "posicao_inicial_jogador_2": self.posicao,
            "vencedor": vencedor.nome,
            "historico": jogo.historico
        })

