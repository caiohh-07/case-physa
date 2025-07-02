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
    print("\nDigite o número da pergunta a ser respondida:")
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

            if modo == "1":
                vitorias_jogador1 = df[df['vencedor'] == 'Jogador 1'].shape[0]
                total_jogos = df['simulacao'].max() + 1
                probabilidade_vitoria_jogador1 = vitorias_jogador1 / total_jogos
                print(f"Resposta: {probabilidade_vitoria_jogador1}")
            else:
                numero_cobras = df.value_counts("evento")
                total_jogos = df['simulacao'].max() + 1
                
                print(f"Resposta: {numero_cobras.iloc[1]/total_jogos}")

            _ = input("\nPressione Enter para continuar...")       

        elif modo == "3":
            df = pd.DataFrame()
            for n in trange(10_000, desc="Simulando escadas com 50% de chance de subir", unit=" jogo"):
                jogo = GameCoditionalClimb(board)
                vencedor = jogo.jogar()
                #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")
                
                hist = pd.DataFrame(print_historico(jogo))
                hist['simulacao'] = n
                df = pd.concat([df, hist])

            turnos_por_simulacao = df.groupby("simulacao")["turno"].count().reset_index()
            qtd_total_turnos = turnos_por_simulacao['turno'].sum()
            qtd_jogos = turnos_por_simulacao['simulacao'].max() + 1
            print(f"Resposta: {qtd_total_turnos/qtd_jogos}")

            _ = input("\nPressione Enter para continuar...") 

        elif modo == "4":
            # Lista fixa de posições iniciais do Jogador 2 (pode ser alterada conforme desejar)
            posicoes = [i for i in range(1,board.size+1)]
            df = pd.DataFrame()

            for posicao in posicoes:
                for n in trange(1_000, desc=f"Começando com jogador 2 na posição {posicao}...", unit=" jogo"):

                    jogo = GameVariableStart(board, posicao)
                    vencedor = jogo.jogar()
                    #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")
                
                    hist = pd.DataFrame(print_historico(jogo))
                    hist['simulacao'] = n
                    hist['posicao_inicial_jogador_2'] = posicao
                    df = pd.concat([df, hist])
            
            # Filtra apenas as linhas onde o jogador 1 foi o vencedor
            vitorias_j1 = df[df["vencedor"] == "Jogador 1"]

            # Conta as vitórias por posição inicial do jogador 1
            contagem = vitorias_j1.groupby("posicao_inicial_jogador_2")["vencedor"].count().reset_index()
            contagem = contagem.rename(columns={"vencedor": "vencedor_jogador_1"})
            qtd_jogos = df['simulacao'].max() + 1
            contagem['prob_vitoria'] = contagem['vencedor_jogador_1'] / qtd_jogos
            contagem['distancia'] = abs(contagem['prob_vitoria'] - 0.5)
            contagem = contagem.sort_values(by='distancia', ascending=True)
            resposta = contagem.iloc[0]['posicao_inicial_jogador_2'].astype(str)

            print(f"Resposta: A posição incial do jogador 2 deveria ser {resposta}")

            _ = input("\nPressione Enter para continuar...")                


        elif modo == "5":
            df = pd.DataFrame()
            for n in trange(10_000, desc="Simulando imunidade à primeira cobra", unit=" jogo"):

                jogo = GameImmuneFirstSnake(board)
                vencedor = jogo.jogar()
                #print(f"\nSimulacao {n} - Vencedor: {vencedor.nome} chegou ou passou da última posição do tabuleiro!")
                
                hist = pd.DataFrame(print_historico(jogo))
                hist['simulacao'] = n
                df = pd.concat([df, hist])

            vitorias_jogador1 = df[df['vencedor'] == 'Jogador 1'].shape[0]
            total_jogos = df['simulacao'].max() + 1
            probabilidade_vitoria_jogador1 = vitorias_jogador1 / total_jogos
            print(f"Resposta: {probabilidade_vitoria_jogador1}")

            _ = input("\nPressione Enter para continuar...") 

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
    print("""   _________         _________
  /         \       /         \   PHYSA.AI
 /  /~~~~~\  \     /  /~~~~~\  \ 
 |  |     |  |     |  |     |  |
 |  |     |  |     |  |     |  |
 |  |     |  |     |  |     |  |         /
 |  |     |  |     |  |     |  |       //
(o  o)    \  \_____/  /     \  \_____/ /
 \__/      \         /       \        /
  |         ~~~~~~~~~         ~~~~~~~~
  ^""")
    main()
