from constants import *
from time import time
from numba import njit, jit
import numpy as np

move_type = MT_NORMAL
num_bot = 0
main_board = np.array([[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]])
line_size = 3
misery = False
num_players = 2
init_bag = np.array([3, 2])
dep = 3

pm = []
nlc = []
ec = []
mv = []
ap = []
bp = []

def draw_txt(board):
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

	@njit
	def possible_moves_normal(player, empty_bag, board):
		#start = time()
		free_cells = np.column_stack(np.where(board == -1))
		if empty_bag:
			owned_cells = np.column_stack(np.where(board == player))
			#pm.append(time()-start)
			arr = np.empty([owned_cells.shape(0) * free_cells.shape(0), 4])
			ind_tot = 0
			for a in range(np.size(owned_cells, 0)):
				for b in range(np.size(free_cells, 0)):
					arr[ind_tot] = np.concatenate((owned_cells[a], free_cells[b]))
					ind_tot += 1
			return arr
		else:
			#pm.append(time()-start)
			return free_cells

	def possible_moves_adj(player, bag, board):
		#usar bag
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

	def possible_moves_gravity(player, bag, board):
		return [(j,) for j in range(len(board[0])) if board[0][j] == -1]

	if move_type == MT_NORMAL:
		return possible_moves_normal
	elif move_type == MT_ADJACENT:
		return possible_moves_adj
	elif move_type == MT_GRAVITY:
		return possible_moves_gravity

possible_moves = possible_moves_generator()

def nline_checker(i, j, board):
	start = time()
	
	def dir_check(mod_i, mod_j, desv):

		if desv >= line_size or \
			i + mod_i*desv < 0 or \
			i + mod_i*desv >= np.size(board, 0) or \
			j + mod_j*desv < 0 or \
			j + mod_j*desv >= np.size(board, 1) or \
			board[i + mod_i*desv, j + mod_j*desv] != board[i, j]:

			return desv-1
		else:
			return dir_check(mod_i, mod_j, desv+1)
	
	if dir_check(0, 1, 1) + dir_check(0, -1, 1) + 1 >= line_size or \
		dir_check(1, 0, 1) + dir_check(-1, 0, 1) + 1 >= line_size or \
		dir_check(1, 1, 1) + dir_check(-1, -1, 1) + 1 >= line_size or \
		dir_check(1, -1, 1) + dir_check(-1, 1, 1) + 1 >= line_size:
		nlc.append(time()-start)
		return board[i, j]
	nlc.append(time()-start)
	return -1

def end_checker(i, j, board):
	start = time()
	check_line = nline_checker(i, j, board)
	if check_line != -1:
		if misery:
			ec.append(time()-start)
			return True, tuple(range(0, check_line)) + tuple(range(check_line+1, num_players+1)), (check_line,)
		else:
			ec.append(time()-start)
			return True, (check_line,), tuple(range(0, check_line)) + tuple(range(check_line+1, num_players+1))
	else:
		ec.append(time()-start)
		return False, None, None

def mindmove(board, player, move):
	start = time()
	l = np.size(move)
	if l == 1:
		i = 0
		j = move[0]
		while i != np.size(board, 0)-1 and board[i+1, j] == -1:
			i += 1
	elif l == 2:
		i = move[0]
		j = move[1]
	elif l == 4:
		i = move[2]
		j = move[3]
		board[move[0], move[1]] = -1
	board[i, j] = player
	mv.append(time()-start)
	return board, i, j

def average_prob(prob_moves):
	start = time()
	average = np.average(prob_moves, axis=0)
	ap.append(time()-start)
	return average

@njit
def best_prob(prob_moves):
	#start = time()
	minimum_lose = np.amin(prob_moves[:, 2])
	less_lose_probs = prob_moves[np.where(prob_moves[:, 2] == minimum_lose)]
	maximum_win_prob = less_lose_probs[np.argmax(less_lose_probs[:, 0])]
	#bp.append(time()-start)
	return maximum_win_prob

diff = [0]*(dep+1)

def bag_resolver(bag):
	if bag[1] == 0:
		bag[1] = num_players
		if bag[0] != 0:
			bag[0] -= 1		

def win_lose_moves(board, pos_moves, depth, num_players, bag, cont_players = 1):
	global diff

	turno = num_players-bag[1]	
	bag[1] -= 1
	
	bag_resolver(bag)

	if cont_players == num_players:
		cont_players = 0

	probs = np.empty([np.size(pos_moves, 0), 3])

	for ind_mov in range(np.size(pos_moves, 0)):
		diff[depth] += 1

		mindboard, i, j = mindmove(board.copy(), turno, pos_moves[ind_mov])
		
		check = end_checker(i, j, mindboard)

		if depth <= 0:
			probs[ind_mov] = np.array([0, 1, 0])
		elif check[0] and num_bot in check[1]:
			probs[ind_mov] = np.array([1, 0, 0])
		elif check[0] and num_bot not in check[1]:
			probs[ind_mov] = np.array([0, 0, 1])		
		else:
			if cont_players != 0:
				probs[ind_mov] = average_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bag[0] == 0, mindboard), depth, num_players, bag.copy(), cont_players+1))
			else:
				probs[ind_mov] = best_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bag[0] == 0, mindboard), depth-1, num_players, bag.copy(), cont_players+1))
	return probs

draw_txt(main_board)

start_g = time()
print(win_lose_moves(main_board, possible_moves(num_bot, init_bag[0] == 0, main_board), dep, 2, init_bag, 1))
print()
print(time()-start_g)

print(diff)

def avg(arr):
	if(len(arr) != 0):
		return sum(arr)/len(arr)
	return -1
print(f"pm: {avg(pm)}, nlc: {avg(nlc)}, ec: {avg(ec)}, mv: {avg(mv)}, ap: {avg(ap)}, bp: {avg(bp)}")
