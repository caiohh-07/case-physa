import json
import random
from datetime import datetime

def carregar_configuracao(caminho_arquivo: str) -> dict:
    """
    Lê o arquivo JSON de configuração do tabuleiro e retorna o dicionário.
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo JSON.
        
    Returns:
        dict: Dicionário com as configurações do tabuleiro.
    """
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def rolar_dado(lados: int = 6) -> int:
    """
    Simula a rolagem de um dado com número de lados definido.
    
    Args:
        lados (int, opcional): Número de lados do dado. Padrão é 6.
        
    Returns:
        int: Valor sorteado entre 1 e 'lados'.
    """
    return random.randint(1, lados)

def gerar_id_simulacao() -> str:
    """
    Gera um ID único para identificar uma simulação, baseado na data e hora atual.
    
    Returns:
        str: ID no formato 'YYYYMMDD_HHMMSSfff'.
    """
    return datetime.now().strftime("%Y%m%d_%H%M%S%f")
