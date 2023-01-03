from abs_board import board_setup, custom_board_checker
from constants import *

#Bucle de selección de variante
wrong_answer = True
while wrong_answer:
    #Imprime las variantes disponibles
    print()
    print("Elige una variante:")
    print()
    for i, v in enumerate(VARIANTS):
        print(str(i+1) + '- ' + v + ':')
        print(VARIANT_DESCRIPTIONS[i])
        print()
    
    #Solicita un número de variante
    sel_variant = input("Introduce un número del 1 al " + str(len(VARIANTS)) + ": ")

    #Lee el número de variante
    try:
        sel_variant = int(sel_variant)
    except:
        #Si el input es incorrecto, se vuelve a solicitar
        print("\n"*200)
        input("Debes introducir un número entero.\nPresiona enter para continuar...")
        continue
    
    #Si el número de variante es incorrecto, se vuelve a solicitar
    if sel_variant < 1 or sel_variant > len(VARIANTS):
        print("\n"*200)
        input("El número introducido debe estar entre 1 y " + str(len(VARIANTS)) + ".\nPresiona enter para continuar...")
        continue
    
    #Si el input es correcto se sale del bucle
    wrong_answer = False

#Si la variante escogida es personalizada, se solicitan los parámetros
if VARIANTS[sel_variant - 1] == 'Custom':

    #Bucle de selección de parámetros
    wrong_answer = True
    while wrong_answer:
        #Imprime las descripciones de los parámetros
        print("\n"*200)
        for i in range(len(CUSTOM_DESCRIPTION)):
            print(CUSTOM_DESCRIPTION[i])
            print()
        
        #Lee los parámetros
        chosen_parameters = input()
        try:
            #Intenta procesar los parámetros
            string_list = chosen_parameters.split()
            custom_tuple = (int(string_list[0]),int(string_list[1]),int(string_list[2]),int(string_list[3]),int(string_list[4]), True if string_list[5] == 'M' else False, MT_NORMAL if string_list[6] == 'N' else MT_ADJACENT if string_list[6] == 'A' else MT_GRAVITY)
            #Si hay parámetros incorrectos, se vuelve a solicitar
            if string_list[5] != 'M' and string_list[5] != 'NM':
                print("\n"*200)
                input("En la sexta posición debes introducir el valor 'M' o 'NM'" + ".\nPresiona enter para continuar...")
                continue
            if string_list[6] != 'N' and string_list[6] != 'A' and string_list[6] != 'G':
                print("\n"*200)
                input("En la séptima posición debes introducir el valor 'N' o 'A' o 'G'" + ".\nPresiona enter para continuar...")
                continue
        except:
            print("\n"*200)
            input("Los datos son incorrectos" + ".\nPresiona enter para continuar...")
            continue

        #Se comprueba que los parámetros sean compatibles y váildos, y si lo son se sale del bucle
        if custom_board_checker(custom_tuple):
            wrong_answer = False
        else:
            print("\n"*200)
            input("Los parámetros introducidos no son compatibles" + ".\nPresiona enter para continuar...")

    #Se asignan los parámetros a la variable setup
    setup = custom_tuple

#Si la variante escogida no es personalizada, se usa una lista de parámetros predefinidos para asignar el correspondiente a setup
else:
    setup = VARIANT_SETUPS[sel_variant - 1]

#Se leen todas las funciones de abs_board usando su función board_setup y pasando los parámetros de setup
board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = board_setup(*setup)

#Por comodidad, se define la variable num_players
num_players = setup[3]

#Se inicializan las variables relacionadas con el bot
bot = False
pos_player = 0
bot_depth = 0

#Bucle para seleccionar si se juega contra la IA o multijugador
wrong_answer = True
while wrong_answer:
    try:
        print("\n"*200)
        print("Deseas jugar multijugador o contra la IA?")
        print("1- Multijugador")
        print("2- Contra la IA")
        sel_num = int(input())
        if(sel_num < 1 or sel_num > 2):
            print("\n"*200)
            input("Debes introducir un número del 1 al 2.\nPresiona enter para continuar...")
        else:
            wrong_answer = False
    except:
        print("\n"*200)
        input("Debes introducir un número entero.\nPresiona enter para continuar...")

#Si se ha seleccionado jugar contra la IA, se solicita la posición del jugador y el nivel de dificultad
if sel_num == 2:
    bot = True

    #Bucle para seleccionar la posición del jugador
    wrong_answer = True
    while wrong_answer:
        try:
            print("\n"*200)
            print(f"¿En qué posición deseas jugar? (1-{num_players})")
            pos_player = int(input()) - 1
            if(pos_player < 0 or pos_player > num_players - 1):
                print("\n"*200)
                input(f"Debes introducir un número del 1 al {num_players}.\nPresiona enter para continuar...")
            else:
                wrong_answer = False
        except:
            print("\n"*200)
            input("Debes introducir un número entero.\nPresiona enter para continuar...")

    #Bucle para seleccionar el nivel de dificultad del bot
    wrong_answer = True
    while wrong_answer:
        try:
            print("\n"*200)
            print(f"¿Qué nivel de dificultad quieres que tenga el bot? (1-3). Introduce -1 para consultar la ayuda")
            bot_depth = int(input())
            if(bot_depth < -1 or bot_depth > 3):
                print("\n"*200)
                input(f"Debes introducir un número del 1 al 3.\nPresiona enter para continuar...")

            #Ofrece una pequeña ayuda para saber qué nivel de dificultad escoger
            elif bot_depth == -1:
                print("\n"*200)
                print("El nivel de dificultad determina la profundidad de búsqueda del bot. La búsqueda tiene una complejidad exponencial, por lo que se debe ajustar este valor con mucho cuidado.")
                print("La cantidad de comprobaciones que hace, viene determinada, más o menos por la fórmula siguiente:")
                print("num_movimientos_posibles ^ (1 + profundidad * num_jugadores)")
                print("Sé prudente escogiendo el nivel o tus partidas no acabarán nunca.")
                input("Presiona enter para continuar...")
            else:
                wrong_answer = False
        except:
            print("\n"*200)
            input("Debes introducir un número entero.\nPresiona enter para continuar...")

#Función que dibuja el tablero en la consola
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

#Función encargada del proceso de selección de una piedra por parte de un jugador
def select_stone_org_txt(player): 

    #Se repite mientras la selección no sea correcta       
    correct_selection = False
    while not correct_selection:
        try:
            #Obtiene las coordenadas de la piedra seleccionada
            org_i, org_j = map(int, input("Selecciona una piedra introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
        except:
            #Si el input no es correcto, se muestra un mensaje de error y se vuelve a pedir el input
            print("\n"*200)
            input("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para continuar...")
            print("\n"*200)
            draw_txt()
            print(f"\nTurno del jugador {player if num_players > 2 else 'O' if player == 0 else 'X'}")
            continue
        
        #Si el input es correcto pero la casilla no está disponible, se muestra un mensaje de error y se vuelve a pedir el input
        if not check_stone(player, org_i, org_j):
            print("\n"*200)
            input("Casilla no disponible.\nPresiona enter para continuar...")
            print("\n"*200)
            draw_txt()
            print(f"\nTurno del jugador {player if num_players > 2 else 'O' if player == 0 else 'X'}")
            continue

        #Si el input es correcto y la casilla está disponible, se marca como correcta la selección y se devuelve la posición de la piedra seleccionada
        correct_selection = True 
    return org_i, org_j

#Función encargada del proceso necesario para mover una piedra por parte de un jugador
def move_txt(player):

    #Se repite mientras el movimiento no sea correcto
    correcto = False
    while not correcto:
        #Se dibuja el tablero
        draw_txt()
        print(f"\nTurno del jugador {player if num_players > 2 else 'O' if player == 0 else 'X'}")

        #Si el tipo de movimiento es distinto del de gravedad
        if setup[6] != MT_GRAVITY:
            #Si el jugador ya ha jugado todas sus piedras, se le pide que seleccione una casilla de origen
            if bag[0] == 0:
                org_i, org_j = select_stone_org_txt(player)

            #Se pide siempre una casilla de destino al jugador
            try:
                dst_i, dst_j = map(int, input("Selecciona una casilla introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
            except:
                print("\n"*200)
                input("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
                continue
            
            #Se crea el movimiento (m) dependiendo de si ha seleccionado o no una piedra de origen
            if bag[0] == 0:
                m = (org_i, org_j, dst_i, dst_j)
            else:
                m = (dst_i, dst_j)
        
        #Si el tipo de movimiento es el de gravedad
        else:
            try:
                #Se pide la columna de destino
                dst_j = int(input("Selecciona una columna introduciendo un número, siendo la columna de la izquierda la 0: "))
            except:
                print("\n"*200)
                input("Columna mal introducida. Debes introducir un único número entero.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
                continue
            
            #Se crea el movimiento (m)
            m = (dst_j,)

        #Se comprueba si el movimiento es correcto             
        correcto = m in possible_moves(player)
        
        #Si no lo es, se muestra un mensaje de error y se vuelve a pedir el input
        if not correcto:
            print("\n"*200)
            input("Movimiento no válido.\nPresiona enter para volver a intentarlo...")
            print("\n"*200)

    #Si el movimiento es correcto, se realiza en el tablero y se devuelve la casilla en la que queda colocada la piedra
    i, j = player_move(m, player)
    return i, j 

#Función encargada de imprimir el o los ganadores de la partida
def print_winner(winners):
    if len(winners) == 1:
        print(f"El jugador {winners[0] if num_players > 2 else 'O' if winners[0] == 0 else 'X'} ha ganado")
    else:
        print("Los jugadores ", end="")
        for w in winners:
            print(f"{w if num_players > 2 else 'O' if w == 0 else 'X'}", end=", " if w != winners[-1] else " ")
        print("han ganado")

#Bucle principal del juego
#Se repite mientras no haya un ganador
end = False
while not end:
    #Para cada jugador
    for p in range(num_players):
        print("\n"*200)
        #Si el turno es del bot (en caso de que lo haya)
        if bot and p != pos_player:
            draw_txt()
            print(f"\nTurno del jugador {p if num_players > 2 else 'O' if p == 0 else 'X'}...")
            #Se realiza el movimiento del bot
            i, j = bot_move(p, bot_depth)      
        else:
            #Si le toca a un jugador humano mover, se llama a la función correspondiente
            i, j = move_txt(p)
        
        #Se comprueba si el movimiento ha provocado un ganador
        win = end_checker(i, j)
        #Si ha habido ganador, se muestra un mensaje y se termina el juego
        if win != -1:
            print("\n"*200)
            draw_txt()
            print_winner(win)
            end = True
            break