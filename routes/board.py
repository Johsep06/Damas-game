from flask import Blueprint, render_template
from src.board import Board
from src.player import Player
from src.ia import IA
from time import sleep

board_route = Blueprint('board', __name__)

def __toString(board:list[list[str]]) -> str:
    s = ''

    for b in board:
        s += ','.join(b) + ';'
    
    s = s[:-1]

    return s

def __toList(string: str) -> list[list[str]]:
    board = []

    string = string.split(';')
    for s in string:
        board.append(s.split(','))

    return board

def get_board() -> list[list[str]]:
    return __board.get_board()

def set_board(new_board:list[list[str]]):
    __board.set_board(new_board)

def playing_ia() -> list[list[str]]:
    __ia.fazer_movimento()

__board = Board()
__board.iniciar_jogo()
__jogador = IA(__board, is_player=True)
__ia = IA(__board, is_player=False)


@board_route.route('/')
def render_board():
    board_str = __toString(get_board())
    return render_template('board.html', board=get_board())

@board_route.route('/', methods=['POST'])
def update_board():
    return render_template('board.html', board=get_board())