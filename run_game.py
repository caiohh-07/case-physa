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
    print("Digite o número da pergunta a ser respondida:")
    print("1 - Num jogo de duas pessoas, qual é a probabilidade do jogador que começa o jogo vencer?")
    print("2 - Em média, em quantas cobras os jogadores caem a cada jogo?")
    print("3 - Se cada vez que um jogador cair em uma escada houver apenas 50% de chance de\n"
        "    ele poder subir, qual é o número médio de lançamentos de dados necessários para completar um jogo?")
    print("4 - Você decide fazer experimentos para que os jogadores tenham aproximadamente\n"
        "    chances iguais de vencerem o jogo. Você faz isso alterando a casa em que o Jogador 2 começa.\n"
        "    Qual casa deveria ser a nova posição inicial do Jogador 2 para que as chances de vitória dos\n"
        "    jogadores sejam aproximadamente iguais?")
    print("5 - Em uma tentativa diferente de alterar as chances do jogo, em vez de mudar a posição\n"
        "    inicial do Jogador 2, você decide dar-lhe imunidade para a primeira cobra em que ele cair. Neste\n"
        "    caso, qual é a probabilidade aproximada de que o Jogador 1 vença?")
    print("0 - Sair")

    modo = input("\nDigite o número do modo desejado: ").strip()
    return modo

def main():
    caminho_tabuleiro = "config/tabuleiro.json"
    board = Board(caminho_tabuleiro)
    modo = ""
    
    while modo != "0":

        modo = escolher_modo()

        if modo == "1" or modo == "2":
            df = pd.DataFrame()
            for n in trange(10_000, desc="Simulando padrão", unit=" jogo"):
                jogo = GameStandard(board)
                vencedor = jogo.jogar()
                #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")

                hist = pd.DataFrame(print_historico(jogo))
                hist['simulacao'] = n
                df = pd.concat([df, hist])
            #df.to_excel('output.xlsx', index=False)
            #print(df.columns)
            #print(df.tail())       

        elif modo == "3":
            df = pd.DataFrame()
            for n in trange(10_000, desc="Simulando escadas com 50% de chance de subir", unit=" jogo"):
                jogo = GameCoditionalClimb(board)
                vencedor = jogo.jogar()
                #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")
                
                hist = pd.DataFrame(print_historico(jogo))
                hist['simulacao'] = n
                df = pd.concat([df, hist])

            #df.to_excel('output.xlsx', index=False)
            #print(df.columns)
            #print(df.tail())

        elif modo == "4":
            # Lista fixa de posições iniciais do Jogador 2 (pode ser alterada conforme desejar)
            posicoes = [i for i in range(1,board.size+1)]

            for posicao in posicoes:
                for n in trange(1_000, desc="Variar posição inicial do jogador 2 e simular múltiplas vezes", unit=" jogo"):

                    jogo = GameVariableStart(board, posicao)
                    vencedor = jogo.jogar()
                    #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")
                
                    hist = pd.DataFrame(print_historico(jogo))
                    hist['simulacao'] = n
                    df = pd.concat([df, hist])
                df['posicao_inicial_jogador_2'] = posicao

            print(df.shape)
            print(df.columns)
            print(df.tail())
                

            for res in jogo_var_start.resultados:
                print(f"\nJogador 2 começou na posição {res['posicao_inicial_jogador_2']} - Vencedor: {res['vencedor']}")
                # for evento in res["historico"]:
                #     print(
                #         f"Rodada {evento['rodada']:>3} | Turno {evento['turno']:>3} | {evento['jogador']}: "
                #         f"Dado={evento['dado']} | Posição {evento['posicao_antes']} -> {evento['posicao_final']} "
                #         f"Evento: {evento['evento']}"
                #     )


        elif modo == "5":
            df = pd.DataFrame()
            for n in trange(10_000, desc="Simulando imunidade à primeira cobra", unit=" jogo"):

                jogo = GameImmuneFirstSnake(board)
                vencedor = jogo.jogar()
                #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")
                
                hist = pd.DataFrame(print_historico(jogo))
                hist['simulacao'] = n
                df = pd.concat([df, hist])

            #df.to_excel('output.xlsx', index=False)
            #print(df.columns)
            #print(df.tail())


        elif modo == "0":
            print("Saindo.")
            sys.exit(1)

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
