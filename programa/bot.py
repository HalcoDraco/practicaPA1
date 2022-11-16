from constants import *
move_type = MT_NORMAL
num_bot = 1
main_board = [[-1, -1, -1],[-1, 0, -1],[-1, -1, -1]]
line_size = 3
misery = False
num_players = 2

def draw_txt(board = main_board):
    for i in board:
        print("+---" * len(i), end="+\n")
        for j in i:
            if num_players == 2:
                if j == 0:
                    print("| O ", end="")
                elif j == 1:
                    print("| X ", end="")
                else:
                    print("|   ", end="")
            else:
                print("| " + (str(j) if j != -1 else " ") + " ", end="")
        print("|")
    print("+---" * len(i), end="+\n")

def possible_moves_generator():
	def possible_moves_normal(player, bag, board = main_board):
		free_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]
		if bag == 0:
			owned_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player]
			return [b + a for a in free_cells for b in owned_cells]
		else:
			return free_cells

	def possible_moves_adj(player, bag, board = main_board):
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

	def possible_moves_gravity(board = main_board):
		return [(j,) for j in range(len(board[0])) if board[0][j] == -1]

	if move_type == MT_NORMAL:
		return possible_moves_normal
	elif move_type == MT_ADJACENT:
		return possible_moves_adj
	elif move_type == MT_GRAVITY:
		return possible_moves_gravity

possible_moves = possible_moves_generator()

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

def end_checker(i, j, board = main_board):
	
	check_line = nline_checker(i, j, board)
	if check_line != -1:
		if misery:
			return True, tuple(range(0, check_line)) + tuple(range(check_line+1, num_players+1)), (check_line,)
		else:
			return True, (check_line,), tuple(range(0, check_line)) + tuple(range(check_line+1, num_players+1))
	else:
		return False, None, None

def mindmove(board, player, bag, move):
	pass

def average_prob(prob_moves):
	average = (0, 0, 0)
	for i in prob_moves:
		average = (average[0] + i[0]/len(prob_moves), average[1] + i[1]/len(prob_moves), average[2] + i[2]/len(prob_moves))
	return average

def best_prob(prob_moves):
	minimum = min(prob_moves, key = lambda x: x[2])
	less_lose = [x for x in prob_moves if x[2] == minimum[2]]
	return max(less_lose, key = lambda x: x[0])

def win_lose_moves(board, pos_moves, depth, num_players, bag, cont_players = 1):

	if cont_players == num_players:
		cont_players = 0

	probs = []
	#pendiente gestionar el bag
	for ind, m in enumerate(pos_moves):
		mindboard = mindmove(board, num_bot, bag, m)
		check = end_checker(m[2], m[3], mindboard)

		if depth <= 0:
			probs[ind] = (0, 1, 0)
		elif check[0] and num_bot in check[1]:
			probs[ind] = (1, 0, 0)
		elif check[0] and num_bot not in check[1]:
			probs[ind] = (0, 0, 1)
		else:
			if cont_players != 0:
				probs[ind] = average_prob(win_lose_moves(mindboard, possible_moves(mindboard), depth, num_players, bag, cont_players+1))
			else:
				probs[ind] = best_prob(win_lose_moves(mindboard, possible_moves(mindboard), depth-1, num_players, bag-1 cont_players+1))
	return probs

possible_moves(num_bot, main_board)
print(win_lose_moves(main_board, possible_moves(num_bot, main_board), 1, 2, 1))
