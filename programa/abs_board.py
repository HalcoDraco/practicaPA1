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

    def possible_moves(player, opt_bag = bag, board = main_board):
        if move_type == MT_NORMAL:
            free_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]
            if opt_bag[0] == 0:
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
            
            return [(x, y) + z for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player for z in free_adj(x, y)] if opt_bag[0] == 0 else [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]

        elif move_type == MT_GRAVITY:
            return [(j,) for j in range(len(board[0])) if board[0][j] == -1]

    def end_checker(i, j, board = main_board):
        if nline_checker(i, j, board) == board[i][j]:
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
            if bag[0] > 0:
                bag[0] -= 1

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
        return board, i, j

    def player_move(m, player):
        i, j = move(m, player)[1:]
        bag[1] -= 1
        bag_resolver(bag)
        return i, j
    
    #bot
    def bot_move(num_bot, depth):
        pm = possible_moves(num_bot)
        all_probs = win_lose_moves(main_board, pm, depth, bag[:], num_bot)
        i, j = move(pm[all_probs.index(best_prob(all_probs))], num_bot)[1:]
        bag[1] -= 1
        bag_resolver(bag)
        return i, j

    def average_prob(prob_moves):
        average = (0, 0, 0)
        l = len(prob_moves)
        for i in prob_moves:
            average = (average[0] + i[0]/l, average[1] + i[1]/l, average[2] + i[2]/l)
        return average

    def best_prob(prob_moves):
        minimum = min(prob_moves, key = lambda x: x[2])
        less_lose = [x for x in prob_moves if x[2] == minimum[2]]
        return max(less_lose, key = lambda x: x[0])

    def win_lose_moves(board, pos_moves, depth, bot_bag, num_bot):
        num_anterior = num_bot-1 if num_bot > 0 else num_players-1
        turno = num_players - bot_bag[1]

        bot_bag[1] -= 1
        bag_resolver(bot_bag)

        probs = []       
        for m in pos_moves:
            board_copy = [row[:] for row in board]
            mindboard, i, j = move(m, turno, board_copy)
            if depth <= 1 and turno == 0:
                pass
            check = end_checker(i, j, mindboard)
            if depth <= 0:
                probs.append((0, 1, 0))
            elif check != -1 and num_bot in check:
                probs.append((1, 0, 0))
            elif check != -1 and num_bot not in check:
                probs.append((0, 0, 1))               
            else:
                bag_copy = bot_bag[:]
                if turno != num_anterior:
                    probs.append(average_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bot_bag, mindboard), depth, bag_copy, num_bot)))
                else:
                    probs.append(best_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bot_bag, mindboard), depth-1, bag_copy, num_bot)))
        return probs

    return main_board, check_stone, possible_moves, player_move, bot_move, end_checker, bag

def custom_board_checker(n):
    if n[3] <= 10 and (n[2] <= n[0] or n[2] <= n[1]) and (n[4] >= n[2] or n[4] == -1) and (n[3] * n[4] <= n[0] * n[1] - 1 or n[4] == -1) and n[0] > 0 and n[1] > 0 and n[2] > 0 and n[3] > 0:
        return True
    return False