class Player:
    def __init__(self, nome: str, posicao_inicial: int = 1, imune_primeira_cobra: bool = False):
        """
        Inicializa um jogador.

        Args:
            nome (str): Nome ou identificação do jogador.
            posicao_inicial (int, opcional): Posição inicial no tabuleiro. Padrão é 1.
        """
        self.nome = nome
        self.posicao = posicao_inicial
        self.imune_primeira_cobra = imune_primeira_cobra  # Inicialmente sem imunidade; modos especiais definem isso

    def mover_para(self, nova_posicao: int):
        """
        Atualiza a posição do jogador.

        Args:
            nova_posicao (int): Nova posição do jogador no tabuleiro.
        """
        self.posicao = nova_posicao

    def remover_imunidade(self):
        """
        Remove a imunidade à primeira cobra após ter sido usada.
        """
        self.imune_primeira_cobra = False

    def resetar(self):
        """
        Reseta o estado do jogador para uma nova partida.
        """
        self.posicao = 0
        self.imune_primeira_cobra = False
