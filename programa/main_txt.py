from abs_board import board_setup
from constants import *

#para vio
def draw_txt():
    """
    Imprime el tablero
    """
    pass

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

setup = VARIANT_SETUPS[sel_variant]
end_checker, move, check_stone = board_setup(*setup)

def select_stone_txt(player):
    draw_txt()
    if setup[6] != MT_GRAVITY and bag == 0:
        #stone selection
        correct_selection = False
        while not correct_selection:
            try:
                org_i, org_j = map(int, input("Selecciona una piedra introduciendo dos coordenadas separadas por un espacio, siendo 0, 0 la esquina superior izquierda: ").split())
            except:
                print("\n"*200)
                print("Coordenadas mal introducidas. El formato de input es 'i j' siendo i y j las dos coordenadas.\nPresiona enter para continuar...")
                continue
            
            if not check_stone(player, org_i, org_j):
                print("\n"*200)
                print("Casilla no disponible.\nPresiona enter para continuar...")
                continue

            correct_selection = True 

def move_txt(player):
    pass


num_players = setup[3]
bag = setup[4]
end = False
while not end:
    for p in range(num_players):

        i, j = move(p)
        end, win, lose = end_checker()
        if end:
            print(win, lose)
            break