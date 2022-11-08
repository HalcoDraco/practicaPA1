def board_setup(board_size_x, board_size_y, line_size):

    board = [[-1]*board_size_y]*board_size_x

    def end_checker():

        for i in range(len(board)):
            consecutive_h = 1
            consecutive_d1 = 1
            consecutive_d2 = 1
            for j in range(1, len(board[0])):

                #comprobación horizontal
                if board[i][j] != -1 and board[i][j] == board[i][j-1]:
                    consecutive_h += 1
                else:
                    consecutive_h = 1

                #comprobación diagonal 1
                if i+j < len(board) and board[i+j][j] != -1 and board[i+j][j] == board[i+j-1][j-1]:
                    consecutive_d1 += 1
                else:
                    consecutive_d1 = 1

                #comprobación diagonal 2
                if i-j >= 0 and board[i-j][j] != -1 and board[i-j][j] == board[i-j+1][j-1]:
                    consecutive_d2 += 1
                else:
                    consecutive_d2 = 1

                if consecutive_h == line_size:
                    return board[i][j]
                if consecutive_d1 == line_size:
                    return board[i+j][j]
                if consecutive_d2 == line_size:
                    return board[i-j][j]
                if consecutive_h > line_size or consecutive_d1 > line_size or consecutive_d2 > line_size:
                    raise Exception("Error al comprobar si el juego ha finalizado. El número de consecutivos es mayor que el número de línea.")

        for j in range(len(board[0])):
            consecutive_v = 1
            consecutive_d1 = 1
            consecutive_d2 = 1
            for i in range(1, len(board)):

                #comprobación vertical
                if board[i][j] != 1 and board[i][j] == board[i-1][j]:
                    consecutive_v += 1
                else:
                    consecutive_v = 1
                
                #comprobación diagonal 1
                if i+j < len(board[0]) and board[i][j+i] != -1 and board[i][j+i] == board[i-1][j+i-1]:
                    consecutive_d1 += 1
                else:
                    consecutive_d1 = 1

                #comprobación diagonal 2
                if j + len(board) - i + 1 < len(board[0]) and board[i][j + len(board) - i] != -1 and board[i][j + len(board) - i] == board[i-1][j + len(board) - i + 1]:
                    consecutive_d2 += 1
                else:
                    consecutive_d2 = 1

                if consecutive_v == line_size:
                    return board[i][j]
                if consecutive_d1 == line_size:
                    return board[i][j+i]
                if consecutive_d2 == line_size:
                    return board[i][j + len(board) - i]
                if consecutive_v > line_size or consecutive_d1 > line_size or consecutive_d2 > line_size:
                    raise Exception("Error al comprobar si el juego ha finalizado. El número de consecutivos es mayor que el número de línea.")

        return -1            

    def mv_stone():
        pass

    def draw_txt():
        pass

def custom_board_checker():
    pass
