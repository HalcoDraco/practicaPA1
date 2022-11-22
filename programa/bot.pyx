from constants import *

move_type = MT_NORMAL

main_board=[[-1]*3 for irow in range(3)]

line_size = 3
misery = True
num_players = 2

dep = 4

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
	def possible_moves_normal(player, bag_emtpy, board):
		free_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]
		if bag_emtpy:
			owned_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player]
			return [b + a for a in free_cells for b in owned_cells]
		else:
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

		""" if desv >= line_size or \
			i + mod_i*desv < 0 or \
			i + mod_i*desv >= len(board) or \
			j + mod_j*desv < 0 or \
			j + mod_j*desv >= len(board[0]) or \
			board[i + mod_i*desv][j + mod_j*desv] != board[i][j]:

			return desv-1
		else:
			return dir_check(mod_i, mod_j, desv+1) """
	
	if dir_check(0, 1) + dir_check(0, -1) + 1 >= line_size or \
		dir_check(1, 0) + dir_check(-1, 0) + 1 >= line_size or \
		dir_check(1, 1) + dir_check(-1, -1) + 1 >= line_size or \
		dir_check(1, -1) + dir_check(-1, 1) + 1 >= line_size:
		return board[i][j]
	return -1

def end_checker(i, j, board):
	check_line = nline_checker(i, j, board)
	if check_line != -1:
		if misery:
			return True, tuple(range(0, check_line)) + tuple(range(check_line+1, num_players)), (check_line,)
		else:
			return True, (check_line,), tuple(range(0, check_line)) + tuple(range(check_line+1, num_players))
	else:
		return False, None, None

def mindmove(board, player, move):
	l = len(move)
	if l == 1:
		i = 0
		j = move[0]
		while i != len(board)-1 and board[i+1][j] == -1:
			i += 1
		board[i][j] = player
	elif l == 2:
		i, j = move[0], move[1]
		board[i][j] = player
	elif l == 4:
		i, j = move[2], move[3]
		board[move[0]][move[1]] = -1
		board[i][j] = player
	return board, i, j

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

diff = [0]*(dep+1)

def bag_resolver(bag):
	if bag[1] == 0:
		bag[1] = num_players	
		if bag[0] != 0:
			bag[0] -= 1



def win_lose_moves(board, pos_moves, depth, bag):
	global diff

	turno = num_players-bag[1]

	bag[1] -= 1

	bag_resolver(bag)

	probs = []
	
	for m in pos_moves:
		
		diff[depth] += 1

		boardt = [row[:] for row in board]
		mindboard, i, j = mindmove(boardt, turno, m)

		check = end_checker(i, j, mindboard)

		if depth <= 0:
			probs.append((0, 1, 0))

		elif check[0] and num_bot in check[1]:
			probs.append((1, 0, 0))

		elif check[0] and num_bot not in check[1]:
			probs.append((0, 0, 1))
			
		else:
			bagt = bag[:]
			if turno != num_anterior:
				probs.append(average_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bag[0] == 0, mindboard), depth, bagt)))
			else:
				probs.append(best_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bag[0] == 0, mindboard), depth-1, bagt)))
	return probs

""" draw_txt(main_board)
print(possible_moves(num_bot, init_bag[0] == 0, main_board))
start = time()
print(win_lose_moves(main_board, possible_moves(num_bot, init_bag[0] == 0, main_board), dep, init_bag))
print(f"Total: {time()-start}")
print(diff)

def avg(arr):
	if(len(arr) != 0):
		return sum(arr)/len(arr)
	return -1
print(f"pm: {avg(pm)}, nlc: {avg(nlc)}, ec: {avg(ec)}, mv: {avg(mv)}, ap: {avg(ap)}, bp: {avg(bp)}") """

end = False
num_bot = 1
init_bag = [4, 2]
""" while not end:
	num_bot = num_players-1-num_bot
	
	num_anterior = num_bot-1 if num_bot > 0 else num_players-1
	init_bag[1] -= 1
	bag_resolver(init_bag)
	po = possible_moves(num_bot, init_bag[0] == 0, main_board)
	if num_bot == 0:
		dep = 4
	else:
		dep = 5
	diff = [0]*(dep+1)
	all_probs = win_lose_moves(main_board, po, dep, init_bag[:])
	main_board, i, j = mindmove(main_board, num_bot, po[all_probs.index(best_prob(all_probs))])
	draw_txt(main_board)
	print(all_probs)
	print("dep: ", dep)
	print(num_bot)
	print(diff)
	print(init_bag)
	check = end_checker(i, j, main_board)
	if check[0] == True:
		print(check[1])
		end = True """
num_bot = 0
num_anterior = num_bot-1 if num_bot > 0 else num_players-1

def main():
	all_probs = win_lose_moves(main_board, possible_moves(num_bot, init_bag[0] == 0, main_board), dep, init_bag[:])
	draw_txt(main_board)
	print(all_probs)
	print("dep: ", dep)
	print(num_bot)
	print(diff)
	print(init_bag)

import cProfile
import pstats

with cProfile.Profile() as pr:
	main()

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
stats.dump_stats(filename="profile.prof")