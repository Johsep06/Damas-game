from src.board import Board
from src.player import Player
from src.ia import IA

def imprimir_tabuleiro(board):
    tabuleiro = board.get_board()
    for linha in tabuleiro:
        print(' '.join(linha if linha else '.' for linha in linha))

def movimento_valido(board:Board, peca:list[int], destino:list[int]):
    movimentos = board.movimentos_possiveis(peca[0], peca[1])
    print(movimentos)
    return destino in movimentos

def main():
    board = Board()
    board.iniciar_jogo()
    
    jogador = Player(board, is_player=True)
    ia = IA(board)

    turno_jogador = True

    while not board.game_over():
        imprimir_tabuleiro(board)
        
        if turno_jogador:
            print("Turno do jogador (Brancas):")
            pecas = jogador.get_pieces()
            print("Peças do jogador:", pecas)

            peca = input("Escolha uma peça (ex: B0): ")
            while peca not in pecas:
                peca = input("Escolha uma peça válida (ex: B0): ")

            movimento = input(f"Escolha um movimento (ex: {board.movimentos_possiveis(pecas[peca][0],pecas[peca][1])}): ")
            destino = [int(x) for x in movimento.split(',')]

            while not movimento_valido(board, pecas[peca], destino):
                movimento = input(f"Escolha um movimento (ex: {board.movimentos_possiveis(pecas[peca][0],pecas[peca][1])}): ")
                destino = [int(x) for x in movimento.split(',')]

            board.mover(pecas[peca], destino)
            jogador.get_pieces()[peca] = destino
        else:
            print("Turno da IA (Pretas):\n\n")
            ia.fazer_movimento()

        turno_jogador = not turno_jogador

        if not jogador.get_pieces() or not ia.get_pieces():
            board.finalizar_jogo()

if __name__ == "__main__":
    main()