from src.board import Board
from src.player import Player
from src.ia import IA

def get_board() -> list[list[str]]:
    return board.get_board()

def set_board(new_board:list[list[str]]):
    board.set_board(new_board)

def playing_ia() -> list[list[str]]:
    ia.fazer_movimento()

board = Board()
board.iniciar_jogo()
jogador = Player(board, is_player=True)
ia = IA(board)

