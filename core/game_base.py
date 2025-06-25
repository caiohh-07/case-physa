from core.board import Board
from core.player import Player
from core.utils import rolar_dado

class GameBase:
    def __init__(self, board: Board):
        """
        Inicializa o jogo base com o tabuleiro e jogadores.

        Args:
            board (Board): Instância do tabuleiro.
        """
        self.board = board
        self.jogadores = [
            Player("Jogador 1"),
            Player("Jogador 2")
        ]
        self.turno = 0
        self.historico = []  # Lista de eventos detalhados (dicionários)

    def jogar_turno(self, jogador: Player):
        """
        Executa o turno de um jogador: rolar dado, mover, aplicar transições.

        Args:
            jogador (Player): Jogador que está jogando.
        """
        self.turno += 1
        pos_antes = jogador.posicao
        dado = rolar_dado()
        pos_dado = pos_antes + dado

        # Não ultrapassar tamanho do tabuleiro
        if pos_dado > self.board.size:
            pos_dado = pos_antes  # fica na mesma casa

        pos_final = self.board.aplicar_transicao(pos_dado)

        # Atualiza posição do jogador
        jogador.mover_para(pos_final)

        # Define evento para o histórico
        if pos_final > pos_dado:
            evento = "escada"
        elif pos_final < pos_dado:
            evento = "cobra"
        else:
            evento = "normal"

        # Registra o evento
        self.historico.append({
            "turno": self.turno,
            "jogador": jogador.nome,
            "posicao_antes": pos_antes,
            "dado": dado,
            "posicao_depois_dado": pos_dado,
            "evento": evento,
            "posicao_final": pos_final,
        })

    def verificar_vencedor(self) -> Player | None:
        """
        Verifica se algum jogador venceu o jogo.

        Returns:
            Player ou None: Jogador vencedor ou None se nenhum venceu ainda.
        """
        for jogador in self.jogadores:
            if jogador.posicao == self.board.size:
                return jogador
        return None

    def jogar(self) -> Player:
        """
        Executa o jogo até que um jogador vença.

        Returns:
            Player: Jogador vencedor.
        """
        indice_jogador = 0
        vencedor = None

        while vencedor is None:
            jogador_atual = self.jogadores[indice_jogador]
            self.jogar_turno(jogador_atual)
            vencedor = self.verificar_vencedor()
            indice_jogador = (indice_jogador + 1) % len(self.jogadores)

        # Marca o vencedor no histórico (última jogada)
        self.historico[-1]["vencedor"] = vencedor.nome
        return vencedor
