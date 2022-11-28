from constants import *
def board_setup(board_size_i, board_size_j, line_size, num_players, num_stones, misery, move_type):

    main_board = [[-1] * board_size_j for x in range(board_size_i)]

    bag = num_stones

    def decrement_bag():
        pass

    def get_bag():
        pass
    
    def get_board():
        return tuple([tuple(x) for x in main_board])

    def nline_checker(i, j, board = main_board):

        def dir_check(mod_i, mod_j, desv):

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

    def put_stone(player, i, j, board = main_board):
        
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == -1:
            board[i][j] = player
            return True
        return False

    def take_stone(player, i, j, board = main_board):
        if check_stone():
            board[i][j] = -1
            return True
        else:
            return False
    
    def check_stone(player, i, j, board = main_board):

        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == player:
            return True
        return False

    #necesario para el bot, opcional para el end_checker
    def possible_moves_generator():
        def possible_moves_normal(player, board = main_board):
            free_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]
            if bag == 0:
                owned_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player]
                return [b + a for a in free_cells for b in owned_cells]
            else:
                return free_cells

        def possible_moves_adj(player, board = main_board):
            def free_adj(i, j):
                free = []
                if i > 0 and board[i-1][j] == -1:
                    free.append((i-1, j))
                if i < len(board)-1 and board[i+1][j] == -1:
                    free.append((i+1, j))
                if j > 0 and board[i][j-1] == -1:
                    free.append((i, j-1))
                if j < len(board[0])-1 and board[i][j+1] == -1:
                    free.append((i, j+1))
                return free
            
            return [(x, y) + z for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player for z in free_adj(x, y)] if bag == 0 else [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]

        def possible_moves_gravity(player, board = main_board):
            return [(j,) for j in range(len(board[0])) if board[0][j] == -1]

        if move_type == MT_NORMAL:
            return possible_moves_normal
        elif move_type == MT_ADJACENT:
            return possible_moves_adj
        elif move_type == MT_GRAVITY:
            return possible_moves_gravity
    
    possible_moves = possible_moves_generator()

    def end_checker(i, j, board = main_board):
        if  nline_checker(i, j) == board[i][j]:
            if misery:
                return [x for x in range(num_players) if x != board[i][j]]
            else:
                return [board[i][j]] 
        elif len(possible_moves(board[i][j])) == 0:
            board[i][j] + 1 if board[i][j] != num_players - 1 else 0
        else:
            return -1


    def move(m, player, board = main_board):
        if len(m) == 1:
            board_rev = board[::-1]
            for k in board_rev:
                if k[m[0]] == -1:
                    board_rev [k][m[0]] == player
            board = board_rev[::-1]
        elif len(m) == 2:
            board[m[0]][m[1]] = player
        else:
            board[m[2]][m[3]] = player
            board[m[0]][m[1]] = -1
        return board, i, j


    return end_checker, move, check_stone, put_stone, get_board, decrement_bag, get_bag

def custom_board_checker(n):
    if n[3] <= 10 and (n[2] <= n[0] or n[2] <= n[1]) and (n[4] >= n[2] or n[4] == -1) and (n[3] * n[4] <= n[0] * n[1] - 1 or n[4] == -1) and n[0] > 0 and n[1] > 0 and n[2] > 0 and n[3] > 0:
        return True
    return False