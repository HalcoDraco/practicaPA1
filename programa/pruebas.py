from random import randint
from constants import *
from time import time
#board = [[randint(-1, 1) for y in range(1000)] for x in range(1000)]
board = [[0, 1, 0, -1, 0, 1, 1], [-1, 1, 1, -1, 1, -1, -1], [0, -1, -1, -1, -1, -1, 1], [1, 0, -1, -1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1], [1, -1, 0, -1, 1, -1, -1]]
move_type = MT_ADJACENT
bag = 3
num_players = 2

def draw_txt():
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
    def possible_moves_normal(player, mindboard):
        free_cells = [(x, y) for x in range(len(mindboard)) for y in range(len(mindboard[0])) if mindboard[x][y] == -1]
        if bag == 0:
            owned_cells = [(x, y) for x in range(len(mindboard)) for y in range(len(mindboard[0])) if mindboard[x][y] == player]
            return [b + a for a in free_cells for b in owned_cells]
        else:
            return free_cells

    def possible_moves_adj(player, mindboard):
        def free_adj(i, j):
            free = []
            if i > 0 and mindboard[i-1][j] == -1:
                free.append((i-1, j))
            if i < len(mindboard)-1 and mindboard[i+1][j] == -1:
                free.append((i+1, j))
            if j > 0 and mindboard[i][j-1] == -1:
                free.append((i, j-1))
            if j < len(mindboard[0])-1 and mindboard[i][j+1] == -1:
                free.append((i, j+1))
            return free
        
        return [(x, y) + z for x in range(len(mindboard)) for y in range(len(mindboard[0])) if mindboard[x][y] == player for z in free_adj(x, y)] if bag == 0 else [(x, y) for x in range(len(mindboard)) for y in range(len(mindboard[0])) if mindboard[x][y] == -1]

    def possible_moves_gravity(player, mindboard):
        return [(j,) for j in range(len(mindboard[0])) if mindboard[0][j] == -1]

    if move_type == MT_NORMAL:
        return possible_moves_normal
    elif move_type == MT_ADJACENT:
        return possible_moves_adj
    elif move_type == MT_GRAVITY:
        return possible_moves_gravity

possible_moves = possible_moves_generator()
print(possible_moves(1))
draw_txt()
