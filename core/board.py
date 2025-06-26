import json

class Board:
    def __init__(self, path_config: str):
        """
        Inicializa o tabuleiro lendo o arquivo JSON.

        Args:
            path_config (str): Caminho para o arquivo JSON de configuração.
        """
        config = self._carregar_configuracao(path_config)
        self.size = config.get("tamanho", 100)
        self.ladders = config.get("escadas", {})
        self.snakes = config.get("cobras", {})
        

    def _carregar_configuracao(self, path: str) -> dict:
        """
        Lê o arquivo JSON e retorna o dicionário de configuração.
        """
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def aplicar_transicao(self, pos: str) -> int:
        """
        Verificar se, ao chegar numa determinada casa do tabuleiro, o
        jogador deve subir uma escada, descer uma cobra ou permanecer na
        mesma posição.
        """
        if pos in self.ladders:
            return self.ladders[pos]
        elif pos in self.snakes:
            return self.snakes[pos]
        else:
            return pos

    def eh_escada(self, pos: int) -> bool:
        return pos in self.ladders

    def eh_cobra(self, pos: int) -> bool:
        return pos in self.snakes
