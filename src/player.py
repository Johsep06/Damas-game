from src.board import Board

class Player(object):
    __player: str
    __board: Board
    
    def __init__(self, board: Board, is_player: bool) -> None:
        self.__board = board
        self.__player = 'B' if is_player else 'P'
        board.set_player(self.__player)
        self.coordenadas = board.get_piece_coord(self.__player)

    def get_pieces(self) -> dict[str, list[int]]:
        return self.coordenadas
    
    def get_board(self) -> Board: return self.__board

    def mover(self, peca: str) -> list[list[int]]:
        peca_coord = self.coordenadas[peca]
        moves = self.__board.movimentos_possiveis(peca_coord[0], peca_coord[1])
        return moves