from abs_board import board_setup
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

#Falta el menú de la variante custom

setup = VARIANT_SETUPS[sel_variant]
end_checker, move, check_stone, put_stone, get_board = board_setup(*setup)
num_players = setup[3]
bag = setup[4]

#para vio
def draw_txt():
    board = get_board()
    for i in board:
        print(i)

def select_stone_org_txt(player):    
    #stone selection
    correct_selection = False
    while not correct_selection:
        draw_txt()
        try:
            org_i, org_j = map(int, input("Selecciona una piedra introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
        except:
            print("\n"*200)
            input("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para continuar...")
            continue
        
        if not check_stone(player, org_i, org_j):
            print("\n"*200)
            print("Casilla no disponible.\nPresiona enter para continuar...")
            continue

        correct_selection = True 
    return org_i, org_j

def move_txt(player):
    correcto = False
    while not correcto:
        #origin selection
        if setup[6] != MT_GRAVITY and bag == 0:
            org_i, org_j = select_stone_org_txt(player)
        
        #destiny selection
        if setup[6] != MT_GRAVITY:
            try:
                dst_i, dst_j = map(int, input("Selecciona una casilla introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
            except:
                print("\n"*200)
                input("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
                continue

            correcto = move(player, org_i, org_j, dst_i, dst_j)

            if not correcto:
                print("\n"*200)
                print("Movimiento no válido.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
        else:
            try:
                dst_j = int(input("Selecciona una columna introduciendo un número, siendo la columna de la izquierda la 0: "))
            except:
                print("\n"*200)
                input("Columna mal introducida. Debes introducir un único número entero.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)
                continue

            correcto, dst_i, dst_j = move(player, dst_j)

            if not correcto:
                print("\n"*200)
                print("Movimiento no válido.\nPresiona enter para volver a intentarlo...")
                print("\n"*200)

    return dst_i, dst_j

end = False
while not end:
    for p in range(num_players):
        i, j = move_txt(p)
        end, win, lose = end_checker()
        if end:
            print(win, lose)
            break