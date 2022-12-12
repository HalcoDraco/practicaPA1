from abs_board import board_setup, custom_board_checker
from constants import *

wrong_answer = True
while wrong_answer:
    print("Elige una variante:")
    print()
    for i, v in enumerate(VARIANTS):
        print(str(i+1) + '- ' + v + ':')
        print(VARIANT_DESCRIPTIONS[i])
        print()
    sel_variant = input("Introduce un número del 1 al " + str(len(VARIANTS)) + ": ")

    try:
        sel_variant = int(sel_variant)
    except:
        print("\n"*200)
        input("Debes introducir un número entero.\nPresiona enter para continuar...")
        continue
    
    if sel_variant < 1 or sel_variant > len(VARIANTS):
        print("\n"*200)
        input("El número introducido debe estar entre 1 y " + str(len(VARIANTS)) + ".\nPresiona enter para continuar...")
        continue
    wrong_answer = False

if VARIANTS[sel_variant - 1] == 'Custom':
    wrong_answer = True
    while wrong_answer:
        print(CUSTOM_DESCRIPTION)
        parametros_escogidos = input()
        try:
            lista_strings = parametros_escogidos.split()
            tupla_custom = (int(lista_strings[0]),int(lista_strings[1]),int(lista_strings[2]),int(lista_strings[3]),int(lista_strings[4]), True if lista_strings[5] == 'M' else False, MT_NORMAL if lista_strings[6] == 'N' else MT_ADJACENT if lista_strings[6] == 'A' else MT_GRAVITY)
            if lista_strings[5] != 'M' and lista_strings[5] != 'NM':
                print("\n"*200)
                input("En la sexta posición debes introducir el valor 'M' o 'NM'" + ".\nPresiona enter para continuar...")
                continue
            if lista_strings[6] != 'N' and lista_strings[6] != 'A' and lista_strings[6] != 'G':
                print("\n"*200)
                input("En la séptima posición debes introducir el valor 'N' o 'A' o 'G'" + ".\nPresiona enter para continuar...")
                continue
        except:
            print("\n"*200)
            input("Los datos son incorrectos" + ".\nPresiona enter para continuar...")
            continue
        if custom_board_checker(tupla_custom):
            wrong_answer = False
    setup = tupla_custom

else:
    setup = VARIANT_SETUPS[sel_variant - 1]

board, check_stone, possible_moves, move, end_checker, bag = board_setup(*setup)
num_players = setup[3]

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

def select_stone_org_txt(player):    
    #stone selection
    correct_selection = False
    while not correct_selection:
        try:
            org_i, org_j = map(int, input("Selecciona una piedra introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
        except:
            print("\n"*200)
            input("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para continuar...")
            print("\n"*200)
            draw_txt()
            print(f"\nTurno del jugador {player if num_players > 2 else 'O' if player == 0 else 'X'}")
            continue
        
        if not check_stone(player, org_i, org_j):
            print("\n"*200)
            input("Casilla no disponible.\nPresiona enter para continuar...")
            print("\n"*200)
            draw_txt()
            print(f"\nTurno del jugador {player if num_players > 2 else 'O' if player == 0 else 'X'}")
            continue

        correct_selection = True 
    return org_i, org_j

def move_txt(player):
    correcto = False
    while not correcto:
        draw_txt()
        print(f"\nTurno del jugador {player if num_players > 2 else 'O' if player == 0 else 'X'}")
        if setup[6] != MT_GRAVITY:
            if bag[0] == 0:
                org_i, org_j = select_stone_org_txt(player)

            try:
                dst_i, dst_j = map(int, input("Selecciona una casilla introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
            except:
                print("\n"*200)
                input("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
                continue

            if bag[0] == 0:
                m = (org_i, org_j, dst_i, dst_j)
            else:
                m = (dst_i, dst_j)                
            correcto = m in possible_moves(player)

            if not correcto:
                print("\n"*200)
                input("Movimiento no válido.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
        else:
            try:
                dst_j = int(input("Selecciona una columna introduciendo un número, siendo la columna de la izquierda la 0: "))
            except:
                print("\n"*200)
                input("Columna mal introducida. Debes introducir un único número entero.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
                continue
            
            m = (dst_j,)
            correcto = m in possible_moves(player)

            if not correcto:
                print("\n"*200)
                print("Movimiento no válido.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)

    i, j = move(m, player)[1:]
    return i, j 

print("\n"*200)
end = False
while not end:
    for p in range(num_players):
        i, j = move_txt(p)
        win = end_checker(i, j)
        if win != -1:
            draw_txt()
            print(f"\nEl jugador {win} ha ganado!")
            end = True
            break