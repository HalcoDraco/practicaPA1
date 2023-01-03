from constants import *
from time import time, sleep

#Función que crea el tablero y las funciones que lo modifican
def board_setup(board_size_i, board_size_j, line_size, num_players, num_stones, misery, move_type):

    #Tablero
    main_board = [[-1] * board_size_j for x in range(board_size_i)]

    #Bolsa de piedras que se encargará de llevar la cuenta del turno y de las piedras que tiene cada jugador
    bag = [num_stones, num_players]

    #Función que comprueba si hay una línea de piedras
    def nline_checker(i, j, board = main_board):

        #Función auxiliar que comprueba si hay una línea de piedras en una dirección
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
        
        #Comprueba todas las direcciones
        if dir_check(0, 1) + dir_check(0, -1) + 1 >= line_size or \
            dir_check(1, 0) + dir_check(-1, 0) + 1 >= line_size or \
            dir_check(1, 1) + dir_check(-1, -1) + 1 >= line_size or \
            dir_check(1, -1) + dir_check(-1, 1) + 1 >= line_size:

            #Si hay línea, devuelve el jugador que la ha hecho
            return board[i][j]

        #Si no, devuelve -1
        return -1

    #Función que comprueba si hay una piedra de un jugador en una posición
    def check_stone(player, i, j, board = main_board):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == player:
            return True
        return False

    #Función que devuelve las posibles jugadas para un jugador
    def possible_moves(player, opt_bag = bag, board = main_board):

        #Si el tipo de movimiento es normal
        if move_type == MT_NORMAL:
            free_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]
            if opt_bag[0] == 0:
                #Si no quedan piedras en la bolsa, devuelve las casillas libres para cada casilla con piedra del jugador
                owned_cells = [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player]
                return [b + a for a in free_cells for b in owned_cells]
            else:
                #Si quedan piedras en la bolsa, devuelve las casillas libres
                return free_cells

        #Si el tipo de movimiento es adyacente
        elif move_type == MT_ADJACENT:

            #Función auxiliar que devuelve las casillas adyacentes libres a una casilla
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
            
            if opt_bag[0] == 0:
                #Si no quedan piedras en la bolsa, devuelve las casillas adyacentes libres para cada casilla con piedra del jugador
                return [(x, y) + z for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == player for z in free_adj(x, y)]
            else:
                #Si quedan piedras en la bolsa, devuelve las casillas libres
                return [(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == -1]

        #Si el tipo de movimiento es gravedad
        elif move_type == MT_GRAVITY:
            #Devuelve las columnas no completas
            return [(j,) for j in range(len(board[0])) if board[0][j] == -1]

    #Función que comprueba si el juego ha terminado
    def end_checker(i, j, board = main_board):

        #Si hay una línea de piedras, devuelve el ganador
        if nline_checker(i, j, board) == board[i][j]:
            if misery:
                #Si el modo de juego es misery, devuelve todos los que no han hecho la línea
                return [x for x in range(num_players) if x != board[i][j]]
            else:
                #Si no, devuelve el que ha hecho la línea
                return [board[i][j]] 
        
        #Si no hay línea, comprueba si quedan movimientos posibles para el siguiente jugador
        elif len(possible_moves(board[i][j] + 1 if board[i][j] != num_players - 1 else 0)) == 0:
            #Si no quedan movimientos, devuelve todos los jugadores excepto el que no tiene movimientos posibles
            return [x for x in range(num_players) if x != (board[i][j] + 1 if board[i][j] != num_players - 1 else 0)]
        else:
            #Si el juego no ha terminado, devuelve -1
            return -1

    #Función que se encarga de actualizar la bolsa de piedras correctamente
    def bag_resolver(bag):
        if bag[1] == 0:
            bag[1] = num_players	
            if bag[0] > 0:
                bag[0] -= 1

    #Función que hace un movimiento en el tablero
    def move(m, player, board = main_board):
        #Dependiendo del movimiento, se actualiza el tablero de una forma u otra

        #Si el movimiento tiene longitud 1, solo puede ser una columna
        if len(m) == 1:
            i = 0
            j = m[0]
            while i != len(board)-1 and board[i+1][j] == -1:
                i += 1
            board[i][j] = player

        #Si el movimiento tiene longitud 2, se está refiriendo a una casilla
        elif len(m) == 2:
            board[m[0]][m[1]] = player
            i = m[0]
            j = m[1]
        
        #Si no, el movimiento tendrá longitud 4, y se estará refiriendo a una casilla origen y una casilla destino
        else:
            board[m[2]][m[3]] = player
            board[m[0]][m[1]] = -1
            i = m[2]
            j = m[3]
        
        #Devuelve la casilla en la que ha quedado colocada la piedra tras el movimiento
        return board, i, j

    #Función que se encarga de hacer un movimiento en el tablero como jugador, es decir, sin usar el bot
    def player_move(m, player):
        #Se limita a hacer el movimiento y actualizar la bolsa
        i, j = move(m, player)[1:]
        bag[1] -= 1
        bag_resolver(bag)
        return i, j


    ##############################
    # Funciones asociadas al bot #
    ##############################

    #Función que se encarga de pensar y hacer un movimiento como bot
    def bot_move(num_bot, depth):
        t1 = time()

        #Obtiene los posibles movimientos
        pm = possible_moves(num_bot)

        #Usando la función win_lose_moves, obtiene las probabilidades de ganar de cada movimiento
        all_probs = win_lose_moves(main_board, pm, depth, bag[:], num_bot)

        #Hace el movimiento con la probabilidad de ganar más alta
        i, j = move(pm[all_probs.index(best_prob(all_probs))], num_bot)[1:]

        #Actualiza la bolsa
        bag[1] -= 1
        bag_resolver(bag)

        #Añade delay si es necesario para que el bot no sea demasiado rápido
        t2 = time()
        if 1 - (t2-t1) > 0:
            sleep(1 - (t2-t1))
        return i, j

    #Función que obtiene la media de una lista de probabilidades
    def average_prob(prob_moves):
        
        #Puesto que esta función se usa durante el turno de los adversarios al bot, 
        #si no hay probabilidades en la lista, y por tanto no hay movimientos posibles, devuelve (1, 0, 0), equivalente a ganar
        l = len(prob_moves)
        if l == 0:
            return (1, 0, 0)

        #Si hay probabilidades, devuelve la media de las probabilidades
        average = (0, 0, 0)
        for i in prob_moves:
            average = (average[0] + i[0]/l, average[1] + i[1]/l, average[2] + i[2]/l)
        return average

    #Función que calcula la mejor probabilidad de una lista de probabilidades
    def best_prob(prob_moves):

        #Puesto que esta función se usa durante el turno del bot,
        #si no hay probabilidades en la lista, y por tanto no hay movimientos posibles, devuelve (0, 0, 1), equivalente a perder
        if len(prob_moves) == 0:
            return (0, 0, 1)

        #Si hay probabilidades, calcula las que tienen menor probabilidad de perder
        minimum = min(prob_moves, key = lambda x: x[2])
        less_lose = [x for x in prob_moves if x[2] == minimum[2]]

        #Devuelve de entre las que tienen menor probabilidad de perder, la que tiene mayor probabilidad de ganar
        return max(less_lose, key = lambda x: x[0])

    #Función recursiva que calcula en árbol las probabilidades de ganar, perder y empatar de cada movimiento posible
    def win_lose_moves(board, pos_moves, depth, bot_bag, num_bot):
        num_anterior = num_bot-1 if num_bot > 0 else num_players-1
        turno = num_players - bot_bag[1]

        bot_bag[1] -= 1
        bag_resolver(bot_bag)

        probs = []
        #Para cada movimiento posible  
        for m in pos_moves:
            board_copy = [row[:] for row in board]

            #Prueba el movimiento en una copia del tablero
            mindboard, i, j = move(m, turno, board_copy)

            #Comprueba si el movimiento gana, pierde o empata
            check = end_checker(i, j, mindboard)
            if depth <= 0:
                probs.append((0, 1, 0))
            elif check != -1 and num_bot in check:
                probs.append((1, 0, 0))
            elif check != -1 and num_bot not in check:
                probs.append((0, 0, 1))               
            else:
                #Si no gana, pierde o empata, se llama a la función de nuevo con el turno del siguiente jugador
                bag_copy = bot_bag[:]
                if turno != num_anterior:
                    probs.append(average_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bot_bag, mindboard), depth, bag_copy, num_bot)))
                else:
                    probs.append(best_prob(win_lose_moves(mindboard, possible_moves(turno+1 if turno+1 < num_players else 0, bot_bag, mindboard), depth-1, bag_copy, num_bot)))
        return probs

    #Finalmente, la función abs_board devuelve todas las funciones que se van a usar en el programa
    return main_board, check_stone, possible_moves, player_move, bot_move, end_checker, bag

#Función que valida una construcción de tablero custom
def custom_board_checker(n):
    #Jugadores de 2 a 10
    #Tablero mínimo de 2x2
    #Mínimo 1 piedra por jugador
    #Tamaño de línea de 1 al máximo de filas o columnas
    #Número de piedras mayor o igual que el tamaño de línea
    #Total de piedras en el tablero menor que el número de casillas
    if n[3] <= 10 \
    and n[3] >= 2 \
    and n[0] >= 2 \
    and n[1] >= 2 \
    and n[2] >= 1 \
    and (n[2] <= max(n[0], n[1])) \
    and (n[4] >= n[2] or n[4] == -1) \
    and (n[3] * n[4] <= n[0] * n[1] - 1 or n[4] == -1):
        return True
    return False