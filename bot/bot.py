def possible_moves(board):
	pass

def move(board, i1, j1, i2, j2):
	return board

def media(prob_moves):
	pass

def mejor(prob_moves):
	pass

def win_lose_moves(pos_moves, depth, num_players, cont_players = 1):

	if cont_players == num_players:
		cont_players = 0

	for m in pos_moves:
		if depth <= 0:
			m[1] = (0, 1, 0)
		elif m == win:
			m[1] = (1, 0, 0)
		elif m == lose:
			m[1] = (0, 0, 1)
		else:
			if cont_players != 0:
				m[1] = media(win_lose_moves(possible_moves(move(board, m)), depth, num_players, cont_players+1))
			else:
				m[1] = mejor(win_lose_moves(possible_moves(move(board, m)), depth-1, num_players, cont_players+1))
	return m

win_lose_moves(movimientos posbiles, 10, 3)