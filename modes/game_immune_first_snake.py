from core.game_base import GameBase
from core.utils import rolar_dado

class GameImmuneFirstSnake(GameBase):
    """
    Modo 4: Cada jogador tem imunidade à primeira cobra que encontrar.
    Na primeira vez que cair em uma cobra, ele ignora a penalidade.
    """

    def jogar_turno(self, jogador):
        self.turno += 1
        pos_antes = jogador.posicao
        dado = rolar_dado()
        pos_dado = pos_antes + dado

        # Se passar do final, fica onde estava
        if pos_dado > self.board.size:
            pos_dado = pos_antes

        evento = "normal"
        pos_final = pos_dado

        if self.board.eh_escada(str(pos_dado)):
            pos_final = self.board.ladders[str(pos_dado)]
            evento = "escada"

        elif self.board.eh_cobra(str(pos_dado)):
            if jogador.imune_primeira_cobra:
                evento = "cobra_ignorada"
                jogador.remover_imunidade()
                pos_final = pos_dado  # permanece onde caiu
            else:
                pos_final = self.board.snakes[str(pos_dado)]
                evento = "cobra"

        jogador.mover_para(pos_final)

        self.historico.append({
            "turno": self.turno,
            "jogador": jogador.nome,
            "posicao_antes": pos_antes,
            "dado": dado,
            "posicao_depois_dado": pos_dado,
            "evento": evento,
            "posicao_final": pos_final
        })
