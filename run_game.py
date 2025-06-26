import sys
import pandas as pd
from tqdm.auto import trange  
from core.board import Board

from modes.game_standard import GameStandard
from modes.game_conditional_climb import GameCoditionalClimb
from modes.game_immune_first_snake import GameImmuneFirstSnake
from modes.game_variable_start import GameVariableStart

import re

def escolher_modo():
    print("Escolha o modo de jogo:")
    print("1 - Padrão (GameStandard)")
    print("2 - Escada com 50% de chance de subir (GameConditionalClimb)")
    print("3 - Variar posição inicial do jogador 2 e simular múltiplas vezes (GameVariableStart)")
    print("4 - Imunidade à primeira cobra (GameImmuneFirstSnake)")
    modo = input("Digite o número do modo desejado: ").strip()
    return modo

def main():
    caminho_tabuleiro = "config/tabuleiro.json"
    board = Board(caminho_tabuleiro)

    modo = escolher_modo()

    if modo == "1":
        df = pd.DataFrame()
        for n in trange(10_000, desc="Simulando jogos", unit=" jogo"):
            jogo = GameStandard(board)
            vencedor = jogo.jogar()
            #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou na casa {vencedor.posicao}!")

            hist = pd.DataFrame(print_historico(jogo))
            hist['simulacao'] = n
            df = pd.concat([df, hist])
        #df.to_excel('output.xlsx', index=False)
        #print(df.columns)
        
        #dados = [parse_event_line(hist[0])]
        #print(dados)

        

    elif modo == "2":
        jogo = GameCoditionalClimb(board)
        vencedor = jogo.jogar()

        print_historico(jogo)
        print(f"\nVencedor: {vencedor.nome} chegou na casa {vencedor.posicao}!")

    elif modo == "3":
        # Lista fixa de posições iniciais do Jogador 2 (pode ser alterada conforme desejar)
        posicoes = [i for i in range(1,37)]

        # Filtra posições inválidas (fora do tabuleiro)
        posicoes = [p for p in posicoes if 1 <= p <= board.size]

        jogo_var_start = GameVariableStart(board, posicoes[0])
        jogo_var_start.jogar()

        for res in jogo_var_start.resultados:
            print(f"\nJogador 2 começou na posição {res['posicao_inicial_jogador_2']} - Vencedor: {res['vencedor']}")
            # for evento in res["historico"]:
            #     print(
            #         f"Rodada {evento['rodada']:>3} | Turno {evento['turno']:>3} | {evento['jogador']}: "
            #         f"Dado={evento['dado']} | Posição {evento['posicao_antes']} -> {evento['posicao_final']} "
            #         f"Evento: {evento['evento']}"
            #     )


    elif modo == "4":
        jogo = GameImmuneFirstSnake(board)
        vencedor = jogo.jogar()

        print_historico(jogo)
        print(f"\nVencedor: {vencedor.nome} chegou na casa {vencedor.posicao}!")

    else:
        print("Modo inválido. Saindo.")
        sys.exit(1)

def print_historico(jogo):
    # print("\nHistórico de jogadas:")
    # for evento in jogo.historico:
    #     print(
    #         f"Rodada {evento['rodada']:>3} | Turno {evento['turno']:>3} | {evento['jogador']}: "
    #         f"Dado={evento['dado']} | Posição {evento['posicao_antes']} -> {evento['posicao_final']} "
    #         f"Evento: {evento['evento']}"
    #     )
    return jogo.historico

if __name__ == "__main__":
    main()
