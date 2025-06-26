import random
from core.game_base import GameBase
from core.utils import rolar_dado

class GameCoditionalClimb(GameBase):
    """
    Modo 2: Jogadores só sobem na escada com 50% de chance.
    Cobras continuam funcionando normalmente.
    """

    def jogar_turno(self, jogador):
        """
        Executa o turno com chance de subir escadas em 50%.
        """
        self.turno += 1
        pos_antes = jogador.posicao
        dado = rolar_dado()
        pos_dado = pos_antes + dado

        if pos_dado > self.board.size:
            pos_dado = pos_antes  # Não ultrapassa o tabuleiro

        # Aplica regra de escada com 50% de chance
        if self.board.eh_escada(str(pos_dado)):
            subir = random.random() > 0.5  # 50% de chance
            if subir:
                pos_final = self.board.ladders[str(pos_dado)]
                evento = "subiu_escada"
            else:
                pos_final = pos_dado
                evento = "não_subiu_escada"
        elif self.board.eh_cobra(str(pos_dado)):
            pos_final = self.board.snakes[str(pos_dado)]
            evento = "cobra"
        else:
            pos_final = pos_dado
            evento = "normal"

        jogador.mover_para(pos_final)

        # Registra evento
        self.historico.append({
            "rodada": self.rodada,
            "turno": self.turno,
            "jogador": jogador.nome,
            "posicao_antes": pos_antes,
            "dado": dado,
            "posicao_depois_dado": pos_dado,
            "evento": evento,
            "posicao_final": pos_final,
        })
