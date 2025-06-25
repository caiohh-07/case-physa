import sys
from core.board import Board

from modes.game_standard import GameStandard
from modes.game_conditional_climb import GameCoditionalClimb
from modes.game_immune_first_snake import GameImmuneFirstSnake
#from modes.game_variable_start import GameVariableStart

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
        jogo = GameStandard(board)
        vencedor = jogo.jogar()

        print_historico(jogo)
        print(f"\nVencedor: {vencedor.nome} chegou na casa {vencedor.posicao}!")

    elif modo == "2":
        jogo = GameCoditionalClimb(board)
        vencedor = jogo.jogar()

        print_historico(jogo)
        print(f"\nVencedor: {vencedor.nome} chegou na casa {vencedor.posicao}!")

    # elif modo == "3":
    #     # Para o modo 3 precisamos pedir a lista de posições iniciais e número de simulações
    #     posicoes_input = input("Digite as posições iniciais do jogador 2, separadas por vírgula (ex: 0,5,10): ")
    #     posicoes = [int(p.strip()) for p in posicoes_input.split(",") if p.strip().isdigit()]

    #     n_sim = input("Digite o número de simulações por posição inicial: ")
    #     n_sim = int(n_sim) if n_sim.isdigit() else 10

    #     modo3 = GameVariableStart(
    #         board_path=caminho_tabuleiro,
    #         posicoes_iniciais=posicoes,
    #         n_simulacoes=n_sim
    #     )
    #     modo3.rodar_simulacoes()

    #     print("\nResultados das simulações:")
    #     for res in modo3.obter_resultados():
    #         print(f"Simulação {res['simulacao_id']}: Jogador 2 começa na casa {res['posicao_inicial_jogador_2']} — Vencedor: {res['vencedor']} em {res['turnos']} turnos")

    elif modo == "4":
        jogo = GameImmuneFirstSnake(board)
        vencedor = jogo.jogar()

        print_historico(jogo)
        print(f"\nVencedor: {vencedor.nome} chegou na casa {vencedor.posicao}!")

    else:
        print("Modo inválido. Saindo.")
        sys.exit(1)

def print_historico(jogo):
    print("\nHistórico de jogadas:")
    for evento in jogo.historico:
        print(
            f"Turno {evento['turno']:>3} | {evento['jogador']}: "
            f"Dado={evento['dado']} | Posição {evento['posicao_antes']} -> {evento['posicao_final']} "
            f"Evento: {evento['evento']}"
        )

if __name__ == "__main__":
    main()
