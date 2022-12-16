from constants import *
def board_setup(board_size_i, board_size_j, line_size, num_players, num_stones, misery, move_type):

    main_board = [[-1] * board_size_j for x in range(board_size_i)]
    bag = [num_stones, num_players]

    def nline_checker(i, j, board = main_board):

        def dir_check(mod_i, mod_j):

            desv = 1
            while not (desv >= line_size or \
                i + mod_i*desv < 0 or \
                i + mod_i*desv >= len(board) or \
                j + mod_j*desv < 0 or \
                j + mod_j*desv >= len(board[0]) or \
                board[i + mod_i*desv][j + mod_j*desv] != board[i][j]):
                desv += 1
            return desv - 1
        
        if dir_check(0, 1) + dir_check(0, -1) + 1 >= line_size or \
            dir_check(1, 0) + dir_check(-1, 0) + 1 >= line_size or \
            dir_check(1, 1) + dir_check(-1, -1) + 1 >= line_size or \
            dir_check(1, -1) + dir_check(-1, 1) + 1 >= line_size:
            return board[i][j]
        return -1

    
    def check_stone(player, i, j, board = main_board):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == player:
            return True
        return False

    def possible_moves(player, board = main_board):
        if move_type == MT_NORMAL:
            free_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]
            if bag[0] == 0:
                owned_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player]
                return [b + a for a in free_cells for b in owned_cells]
            else:
                return free_cells

        elif move_type == MT_ADJACENT:
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
            
            return [(x, y) + z for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player for z in free_adj(x, y)] if bag[0] == 0 else [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]

        elif move_type == MT_GRAVITY:
            return [(j,) for j in range(len(board[0])) if board[0][j] == -1]

    def end_checker(i, j, board = main_board):
        if nline_checker(i, j) == board[i][j]:
            if misery:
                return [x for x in range(num_players) if x != board[i][j]]
            else:
                return [board[i][j]] 
        elif len(possible_moves(board[i][j] + 1 if board[i][j] != num_players - 1 else 0)) == 0:
            return [x for x in range(num_players) if x != (board[i][j] + 1 if board[i][j] != num_players - 1 else 0)]
        else:
            return -1

    def bag_resolver(bag):
        if bag[1] == 0:
            bag[1] = num_players	
            if bag[0] != 0:
                bag[0] -= 1

    #nota para pablo: cambiar bag para el bot
    def move(m, player, board = main_board):
        if len(m) == 1:
            i = 0
            j = m[0]
            while i != len(board)-1 and board[i+1][j] == -1:
                i += 1
            board[i][j] = player
        elif len(m) == 2:
            board[m[0]][m[1]] = player
            i = m[0]
            j = m[1]
        else:
            board[m[2]][m[3]] = player
            board[m[0]][m[1]] = -1
            i = m[2]
            j = m[3]
        bag[1] -= 1
        bag_resolver(bag)
        return board, i, j
    return main_board, check_stone, possible_moves, move, end_checker, bag

def custom_board_checker(n):
    if n[3] <= 10 and (n[2] <= n[0] or n[2] <= n[1]) and (n[4] >= n[2] or n[4] == -1) and (n[3] * n[4] <= n[0] * n[1] - 1 or n[4] == -1) and n[0] > 0 and n[1] > 0 and n[2] > 0 and n[3] > 0:
        return True
    return False