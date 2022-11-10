from constants import *
def board_setup(board_size_i, board_size_j, line_size, num_players, num_stones, misery, move_type):

    board = [[-1]*board_size_j]*board_size_i

    bag = num_stones

    def nline_checker(i, j):
        """
        Comprueba si existe un n en raya partiendo de la casilla a la que se ha movido una piedra
        Para ello hace uso de una fucnión recursiva que se ejecutará en cada una de las 4 direcciones, en ambos sentidos
        i y j determinarán la posición a la que se ha movido la última piedra
        Hace return del jugador ganador si hay un n en raya o de -1 si no lo hay
        """

        def dir_check(mod_i, mod_j, desv):
            """
            Cuenta de manera recursiva el número de casillas iguales a la escogida (board[i][j]) en una dirección y en un sentido
            mod_i y mod_j determinarán la dirección y sentido en la que avanzará el recuento
            desv será el número de casillas avanzadas
            Hace return del número de casillas iguales a la i, j en la dirección y sentido seleccionados
            """

            if desv >= line_size or \
                i + mod_i*desv < 0 or \
                i + mod_i*desv >= len(board) or \
                j + mod_j*desv < 0 or \
                j + mod_j*desv >= len(board[0]) or \
                board[i + mod_i*desv][j + mod_j*desv] != board[i][j]:

                return desv-1
            else:
                return dir_check(mod_i, mod_j, desv+1)
        
        if dir_check(0, 1, 1) + dir_check(0, -1, 1) + 1 >= line_size or \
            dir_check(1, 0, 1) + dir_check(-1, 0, 1) + 1 >= line_size or \
            dir_check(1, 1, 1) + dir_check(-1, -1, 1) + 1 >= line_size or \
            dir_check(1, -1, 1) + dir_check(-1, 1, 1) + 1 >= line_size:

            return board[i][j]
        return -1

    def put_stone(n, i, j):
        """
        Pone una piedra en la casilla i, j si la posición es válida y no hay ninguna antes.
        i y j determinarán la posición para poner la piedra
        n será el jugador que pone la piedra
        """
        
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == -1:
            board[i][j] = n
            return True
        return False
    
    def check_stone(n, i, j):
        """
        Comprueba si la casilla i, j del tablero está ocupada por una piedra del jugador n
        Devuelve True en caso de que esté ocupada por una piedra del jugador n y false en caso contrario
        """

        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == n:
            return True
        return False

    
    def end_checker():
        pass  

    def move_generator():
        def move_normal():
            pass  

        def move_adj():
            pass

        def move_gravity():
            pass

        if move_type == MT_NORMAL:
            return move_normal
        elif move_type == MT_ADJACENT:
            return move_adj
        elif move_type == MT_GRAVITY:
            return move_gravity
        


    

  
        

                

    return end_checker, move, draw_txt

def custom_board_checker():
    pass
