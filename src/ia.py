from src.player import Player
from src.board import Board

class IA(Player):
    def __init__(self, board: Board) -> None:
        super().__init__(board, is_player=False)
    
    def escolher_movimento(self) -> tuple[str, list[int]]:
        melhor_movimento = None
        melhor_pontuacao = float('-inf')
        
        for peca, coord in self.get_pieces().items():
            movimentos = self.get_board().movimentos_possiveis(coord[0], coord[1])
            for movimento in movimentos:
                pontuacao = self.avaliar_movimento(coord, movimento)
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_movimento = (peca, movimento)
        
        return melhor_movimento
    
    def avaliar_movimento(self, pos_inicial: list[int], pos_final: list[int]) -> int:
        peca_destino = self.get_board().get_board()[pos_final[0]][pos_final[1]]
        if peca_destino == '':
            return 1
        elif peca_destino[0] != 'P':  
            return 5

        return 0
    
    def fazer_movimento(self) -> None:
        peca, movimento = self.escolher_movimento()
        if peca and movimento:
            self.get_board().mover(self.coordenadas[peca], movimento)
            self.coordenadas[peca] = movimento
        else:
            self.__board.finalizar_jogo()
            print("IA não tem movimentos possíveis. O jogo terminou.")
