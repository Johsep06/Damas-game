class Board(object):
    __board = [['' for j in range(8)] for i in range(8)]
    __game_over = False
    
    def __init__(self) -> None:
        pass

    def game_over(self): return self.__game_over

    def get_board(self):
        return self.__board
    
    def set_board(self, board:list[list[str]]):
        self.__board = board
    
    def static_board(self) -> list[list[str]]:
        board = [
            ['','P00','','P10','','P20','','P30'],
            ['P40','','P50','','P60','','P70',''],
            ['','P80','','P90','','Pa0','','Pb0'],
            ['','','','','','','',''],
            ['','','','B10','','','',''],
            ['B00','','','','B20','','B30',''],
            ['','B40','','B50','','B60','','B70'],
            ['B80','','B90','','Ba0','','Bb0','']
        ]
        return board
    
    def set_player(self, player: str) -> bool:
        ids = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b']
        start, stop = -1, -1

        if player == 'B': 
            start, stop = 5, 8
        elif player == 'P': 
            start, stop = 0, 3

        if start == -1: 
            return False

        cont = 0
        for i in range(start, stop):
            aux = i % 2 - 1
            for j in range(4):
                self.__board[i][j * 2 - aux] = player + ids[cont] + '0'
                cont += 1

        return True
    
    def get_piece_coord(self, player: str) -> dict[str, list[int]]:
        coordenadas = {}
        for i in range(8):
            for j in range(8):
                if player in self.__board[i][j]:
                    coordenadas[self.__board[i][j][:-1]] = [i, j]
        return coordenadas
    
    def __direcao(self, pos: list[int], direcao: str) -> list[int]:
        nova_pos = []
        if direcao == 'N':
            nova_pos.append(pos[0] + 1)
            nova_pos.append(pos[1] + 1)
        elif direcao == 'S':
            nova_pos.append(pos[0] - 1)
            nova_pos.append(pos[1] - 1)
        elif direcao == 'L':
            nova_pos.append(pos[0] - 1)
            nova_pos.append(pos[1] + 1)
        elif direcao == 'O':
            nova_pos.append(pos[0] + 1)
            nova_pos.append(pos[1] - 1)

        return nova_pos
    
    def mover(self, peca: list[int], move:list[int]) -> list[int]:
        if self.__game_over:
            raise Exception("O jogo já terminou. Reinicie para jogar novamente.")
        
        self.__board[move[0]][move[1]] = self.__board[peca[0]][peca[1]]
        self.__board[peca[0]][peca[1]] = ''
        
        self.promover_a_dama(move)
        return move
    
    def verifica_move(self, pos: list[int], direcao: str, recursivo: bool = False) -> str:
        piece = self.__board[pos[0]][pos[1]]
        move = ''
        
        if piece[-1] == '0':
            prox = self.__direcao(pos, direcao)
            if not self.__dentro_do_tabuleiro(prox[0], prox[1]) or self.__board[prox[0]][prox[1]] != '':
                return move

            move = direcao
        return move
    
    def get_moves(self, pieces: dict[str, list[int]]) -> dict[str, str]:
        keys = list(pieces.keys())
        moves = {}

        for k in keys:
            moves[k] = []
            pos = pieces[k]
            if self.__board[pos[0]][pos[1]][-1] == '0':
                if pos[0] > 0 and pos[1] > 0 and self.__board[pos[0] - 1][pos[1] - 1] == '':
                    moves[k].append('O')

                if pos[0] > 0 and pos[1] < 7 and self.__board[pos[0] - 1][pos[1] + 1] == '':
                    moves[k].append('N')

                if pos[0] < 7 and pos[1] > 0 and self.__board[pos[0] + 1][pos[1] - 1] == '':
                    moves[k].append('S')

                if pos[0] < 7 and pos[1] < 7 and self.__board[pos[0] + 1][pos[1] + 1] == '':
                    moves[k].append('L')

        return moves

    def __dentro_do_tabuleiro(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.__board) and 0 <= y < len(self.__board[0])

    def movimentos_possiveis(self, linha: int, coluna: int) -> list[list[int]]:
        tabuleiro = self.get_board()
        
        movimentos = []
        peca = tabuleiro[linha][coluna]
        
        if peca == '':
            return movimentos
        
        cor = peca[0]
        tipo = peca[2]
        
        direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        if tipo == '0':  
            if cor == 'B':
                direcoes = [(-1, -1), (-1, 1)]
            else:
                direcoes = [(1, -1), (1, 1)]
        
        for dx, dy in direcoes:
            nx, ny = linha + dx, coluna + dy
            if self.__dentro_do_tabuleiro(nx, ny):
                if tabuleiro[nx][ny] == '':
                    movimentos.append([nx, ny])
                elif tabuleiro[nx][ny][0] != cor:
                    # Verifica a captura
                    nx2, ny2 = nx + dx, ny + dy
                    if self.__dentro_do_tabuleiro(nx2, ny2) and tabuleiro[nx2][ny2] == '':
                        movimentos.append([nx2, ny2])
        
        return movimentos

    def promover_a_dama(self, pos: list[int]) -> None:
        linha, coluna = pos
        peca = self.__board[linha][coluna]
        
        if (peca[0] == 'P' and linha == 7) or (peca[0] == 'B' and linha == 0):
            self.__board[linha][coluna] = peca[:2] + '1'

    def finalizar_jogo(self) -> None:
        self.__game_over = True
        print("O jogo terminou.")

    def reiniciar_jogo(self) -> None:
        self.__board = [['' for j in range(8)] for i in range(8)]
        self.__game_over = False

    def iniciar_jogo(self) -> None:
        self.reiniciar_jogo()
        self.set_player('B')
        self.set_player('P')
        self.__game_over = False