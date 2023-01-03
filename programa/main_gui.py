import pygame
from constants import *
from abs_board import board_setup, custom_board_checker

#############
# Funciones #
#############

#Función para cargar la pantalla de inicio
def start_screen():
    global main_screen, actual_interface

    #Cambia la interfaz actual
    actual_interface = START_INTERFACE

    #Inicialización de la pantalla
    main_screen = pygame.display.set_mode((START_WINDOW_WIDTH, START_WINDOW_HEIGHT))
    main_screen.fill(BACKGROUND_COLOR)

    #Inicialización de los textos
    text = big_font.render('Escoge el modo de juego:', False, TEXT_COLOR)
    help = big_font.render('?', False, TEXT_COLOR)
    num1_txt = big_font.render('Normal', False, TEXT_COLOR)
    num2_txt = big_font.render('Misery', False, TEXT_COLOR)
    num3_txt = big_font.render('Adyacente', False, TEXT_COLOR)
    num4_txt = big_font.render('Misery ady', False, TEXT_COLOR)
    num5_txt = big_font.render('4 en raya', False, TEXT_COLOR)
    num6_txt = big_font.render('Custom', False, TEXT_COLOR)

    #Pinta los botones
    pygame.draw.rect(main_screen, GREY, button1)
    pygame.draw.rect(main_screen, GREY, button2)
    pygame.draw.rect(main_screen, GREY, button3)
    pygame.draw.rect(main_screen, GREY, button4)
    pygame.draw.rect(main_screen, GREY, button5)
    pygame.draw.rect(main_screen, GREY, button6)
    pygame.draw.rect(main_screen, LIGHT_GREY, button_help)

    #Pinta los textos
    main_screen.blit(text, (PADDING*3, PADDING*3))
    main_screen.blit(help, help.get_rect(center = (START_WINDOW_WIDTH - PADDING*3 - HELP_BUTTON_SIZE//2, PADDING*3 + HELP_BUTTON_SIZE//2)))
    main_screen.blit(num1_txt, num1_txt.get_rect(center = (PADDING*3 + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//4 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num2_txt, num2_txt.get_rect(center = (PADDING*3 + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//2 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num3_txt, num3_txt.get_rect(center = (PADDING*3 + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)*3//4 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num4_txt, num4_txt.get_rect(center = (START_WINDOW_WIDTH//2 + PADDING + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//4 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num5_txt, num5_txt.get_rect(center = (START_WINDOW_WIDTH//2 + PADDING + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//2 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num6_txt, num6_txt.get_rect(center = (START_WINDOW_WIDTH//2 + PADDING + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)*3//4 + BIG_BUTTON_HEIGHT//2)))

#Función para cargar la pantalla de crear un juego 
def custom_board():
    global main_screen, actual_interface

    #Borra lo anterior de la pantalla
    main_screen.fill(BACKGROUND_COLOR)

    #Cambia la interfaz actual
    actual_interface = CUSTOM_INTERFACE

    #Creación de los textos
    s_suma = big_font.render('+', False, TEXT_COLOR)
    s_resta = big_font.render('-', False, TEXT_COLOR)

    n_filas_txt = big_font.render('Número de filas', False, TEXT_COLOR)
    main_screen.blit(n_filas_txt, (PADDING*2, PADDING))
    n_columnas_txt = big_font.render('Número de columnas', False, TEXT_COLOR)
    main_screen.blit(n_columnas_txt, (PADDING*2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)//8))
    n_en_raya_txt = big_font.render('N en raya', False, TEXT_COLOR)
    main_screen.blit(n_en_raya_txt, (PADDING*2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*2//8))
    n_jugadores_txt = big_font.render('Número de jugadores', False, TEXT_COLOR)
    main_screen.blit(n_jugadores_txt, (PADDING*2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*3//8))
    n_piedras_txt = big_font.render('Número de piedras', False, TEXT_COLOR)
    main_screen.blit(n_piedras_txt, (PADDING*2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*4//8))
    misery_txt = big_font.render('Variante misery', False, TEXT_COLOR)
    main_screen.blit(misery_txt, (PADDING*2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*5//8))
    movimiento_txt = big_font.render('Tipo de movimiento', False, TEXT_COLOR)
    main_screen.blit(movimiento_txt, (PADDING*2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*6//8))
    continuar_txt = big_font.render('Continuar', False, TEXT_COLOR)

    #Pinta los botones
    pygame.draw.rect(main_screen, GREY, button_dec_num_rows)
    pygame.draw.rect(main_screen, GREY, button_inc_num_rows)
    pygame.draw.rect(main_screen, GREY, button_dec_num_columns)
    pygame.draw.rect(main_screen, GREY, button_inc_num_columns)
    pygame.draw.rect(main_screen, GREY, button_dec_line_size)
    pygame.draw.rect(main_screen, GREY, button_inc_line_size)
    pygame.draw.rect(main_screen, GREY, button_dec_num_players)
    pygame.draw.rect(main_screen, GREY, button_inc_num_players)
    pygame.draw.rect(main_screen, GREY, button_dec_num_stones)
    pygame.draw.rect(main_screen, GREY, button_inc_num_stones)
    pygame.draw.rect(main_screen, GREY, button_dec_misery)
    pygame.draw.rect(main_screen, GREY, button_inc_misery)
    pygame.draw.rect(main_screen, GREY, button_dec_move_type)
    pygame.draw.rect(main_screen, GREY, button_inc_move_type)
    pygame.draw.rect(main_screen, GREY, button_custom_continue)

    #Pinta los textos de incremento y decremento y el de continuar
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*2//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*3//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*4//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*5//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_resta, s_resta.get_rect(center = (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*6//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*2//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*3//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*4//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*5//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(s_suma, s_suma.get_rect(center = (START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*6//8 + XS_BUTTON_SIZE//2)))
    main_screen.blit(continuar_txt, continuar_txt.get_rect(center = (START_WINDOW_WIDTH//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*7//8 + MEDIUM_BUTTON_HEIGHT//2)))

    #Actualiza los valores en la pantalla
    update_values_custom()

#Función auxiliar para renderizar texto en varias líneas
def multi_line_renderer(text, font, color, surface, x, y, line_spacing = 0):
    lines = text.splitlines()
    for line in lines:
        surface.blit(font.render(line, False, color), (x, y))
        y += font.get_linesize() + line_spacing

#Función que renderiza la pantalla de ayuda
def help_screen():
    global main_screen, actual_interface

    #Borra lo que haya en la pantalla
    main_screen.fill(BACKGROUND_COLOR)

    #Actualiza la interfaz actual
    actual_interface = HELP_INTERFACE

    multi_line_renderer(CUSTOM_DESCRIPTION[3], medium_font, TEXT_COLOR, main_screen, PADDING, PADDING)

    #Botón de volver
    pygame.draw.rect(main_screen, GREY, button_go_back)
    go_back_txt = big_font.render('Volver', False, TEXT_COLOR)
    main_screen.blit(go_back_txt, go_back_txt.get_rect(center = (START_WINDOW_WIDTH//2, START_WINDOW_HEIGHT - MEDIUM_BUTTON_HEIGHT//2 - PADDING)))

#Función que carga la variante seleccionada o carga la pantalla de selección custom
def set_setup(num):
    global setup, board, check_stone, possible_moves, player_move, bot_move, end_checker, bag, num_players
    if num != 5:
        #Si no es la variante custom, carga la variante seleccionada
        setup = VARIANT_SETUPS[num]
        board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = board_setup(*setup)
        num_players = setup[3]
        select_bot_multi()
    else:
        #Si es la variante custom, carga la pantalla de selección custom
        custom_board()

#Función que carga la pantalla que permite seleccionar si se juega contra un bot o contra otro jugador
def select_bot_multi():
    global main_screen, actual_interface
    #Borra lo que haya en la pantalla
    main_screen.fill(BACKGROUND_COLOR)
    #Actualiza la interfaz actual
    actual_interface = SELECT_BOT_INTERFACE

    #Botones de selección
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_multiplayer)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_bot)
    text = big_font.render('Multiplayer', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_multiplayer.centerx, button_multiplayer.centery)))
    text = big_font.render('Bot', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_bot.centerx, button_bot.centery)))

#Función que carga la pantalla de selección de dificultad del bot y posición del jugador
def setup_bot():
    global main_screen, actual_interface
    #Borra lo que haya en la pantalla
    main_screen.fill(BACKGROUND_COLOR)
    #Actualiza la interfaz actual
    actual_interface = BOT_SETUP_INTERFACE

    #Botones y textos
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_dec_depth)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_inc_depth)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_dec_pos_player)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_inc_pos_player)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_bot_continue)
    text = big_font.render('Dificultad del bot', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, START_WINDOW_HEIGHT//6)))
    text = big_font.render('Turno del jugador', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 3*START_WINDOW_HEIGHT//6)))
    text = big_font.render('-', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_dec_depth.centerx, button_dec_depth.centery)))
    main_screen.blit(text, text.get_rect(center = (button_dec_pos_player.centerx, button_dec_pos_player.centery)))
    text = big_font.render('+', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_inc_depth.centerx, button_inc_depth.centery)))
    main_screen.blit(text, text.get_rect(center = (button_inc_pos_player.centerx, button_inc_pos_player.centery)))
    text = big_font.render('Continuar', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_bot_continue.centerx, button_bot_continue.centery)))

    #Actualiza los valores en pantalla
    update_values_bot()

#Función que se encarga de actualizar los valores en pantalla de la interfaz de selección de dificultad del bot y posición del jugador
def update_values_bot():
    global main_screen
    text = big_font.render(str(bot_depth), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 2*START_WINDOW_HEIGHT//6)))
    text = big_font.render(str(pos_player+1), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 4*START_WINDOW_HEIGHT//6)))

#Función que se encarga de actualizar los valores en pantalla de la interfaz de selección custom
def update_values_custom():
    global main_screen

    #Borra los valores anteriores
    rectangulo = pygame.Rect(0, 0, 100, START_WINDOW_HEIGHT)
    rectangulo.centerx = START_WINDOW_WIDTH*5//6 - PADDING//2
    pygame.draw.rect(main_screen, BACKGROUND_COLOR, rectangulo)
    pygame.draw.rect(main_screen, BACKGROUND_COLOR, pygame.Rect(START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*7//8 + MEDIUM_BUTTON_HEIGHT//4, MEDIUM_BUTTON_WIDHT, MEDIUM_BUTTON_HEIGHT))

    #Escribe los nuevos valores
    text = big_font.render(str(num_rows), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + XS_BUTTON_SIZE//2)))
    text = big_font.render(str(num_columns), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + (START_WINDOW_HEIGHT - PADDING*2)//8 + XS_BUTTON_SIZE//2)))
    text = big_font.render(str(line_size), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*2//8 + XS_BUTTON_SIZE//2)))
    text = big_font.render(str(num_players), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*3//8 + XS_BUTTON_SIZE//2)))
    text = big_font.render(str(num_stones) if num_stones != -1 else "inf", True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*4//8 + XS_BUTTON_SIZE//2)))
    text = big_font.render("Sí" if misery == True else "No", True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*5//8 + XS_BUTTON_SIZE//2)))
    text = big_font.render("Norm" if move_type == MT_NORMAL else "Ady" if move_type == MT_ADJACENT else "Grav", True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH*5//6 - PADDING, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*6//8 + XS_BUTTON_SIZE//2)))


#Funciones que se encargan de modificar los valores de las variables globales

def mod_num_rows(inc):
    global num_rows
    if inc:
        if num_rows < 10:
            num_rows += 1
    else:
        if num_rows > 1:
            num_rows -= 1
    update_values_custom()

def mod_num_columns(inc):
    global num_columns
    if inc:
        if num_columns < 10:
            num_columns += 1
    else:
        if num_columns > 1:
            num_columns -= 1
    update_values_custom()

def mod_line_size(inc):
    global line_size
    if inc:
        if line_size < 10:
            line_size += 1
    else:
        if line_size > 1:
            line_size -= 1
    update_values_custom()

def mod_num_players(inc):
    global num_players
    if inc:
        if num_players < 10:
            num_players += 1
    else:
        if num_players > 1:
            num_players -= 1
    update_values_custom()

def mod_num_stones(inc):
    global num_stones
    if inc:        
        if num_stones == 49:
            num_stones = -1
        elif num_stones == -1:
            num_stones = 1
        elif num_stones < 49:
            num_stones += 1
    else:        
        if num_stones == 1:
            num_stones = -1
        elif num_stones == -1:
            num_stones = 49
        elif num_stones > 1:
            num_stones -= 1     
    update_values_custom()

def mod_misery():
    global misery
    misery = not misery
    update_values_custom()

def mod_move_type(inc):
    global move_type
    if inc:
        if move_type == MT_NORMAL:
            move_type = MT_ADJACENT
        elif move_type == MT_ADJACENT:
            move_type = MT_GRAVITY
        elif move_type == MT_GRAVITY:
            move_type = MT_NORMAL
    else:
        if move_type == MT_NORMAL:
            move_type = MT_GRAVITY
        elif move_type == MT_ADJACENT:
            move_type = MT_NORMAL
        elif move_type == MT_GRAVITY:
            move_type = MT_ADJACENT
    update_values_custom()

def mod_bot_depth(inc):
    global bot_depth
    if inc:
        if bot_depth < 3:
            bot_depth += 1
    else:
        if bot_depth > 0:
            bot_depth -= 1
    update_values_bot()

def mod_pos_player(inc):
    global pos_player
    if inc:
        if pos_player < num_players - 1:
            pos_player += 1
    else:
        if pos_player > 0:
            pos_player -= 1
    update_values_bot()

#Función que gestiona la acción de continuar en la pantalla de configuración de partida custom
def custom_continue():
    global setup, board, check_stone, possible_moves, player_move, bot_move, end_checker, bag, main_screen, num_players
    setup = (num_rows, num_columns, line_size, num_players, num_stones, misery, move_type)
    if custom_board_checker(setup):       
        board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = board_setup(*setup)
        num_players = setup[3]
        select_bot_multi()
    else:
        wrong_values_txt = medium_font.render('Valores erróneos', False, RED)
        main_screen.blit(wrong_values_txt, (START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*7//8 + MEDIUM_BUTTON_HEIGHT//4))

#Función que inicia el juego
def setup_game(use_bot):
    global main_screen, actual_interface, bot
    bot = use_bot
    main_screen = pygame.display.set_mode((len(board[0])*(PADDING_SQUARE + SQUARE_SIZE) + PADDING_SQUARE, len(board)*(PADDING_SQUARE + SQUARE_SIZE) + 2*PADDING_SQUARE + SQUARE_SIZE))
    draw_gui()
    actual_interface = GAME_INTERFACE
    
#Función que traduce coordenadas de índice a pixel
def translate_coords_itp(i, j):
    return (PADDING_SQUARE + (PADDING_SQUARE + SQUARE_SIZE)*j, PADDING_SQUARE + (PADDING_SQUARE + SQUARE_SIZE)*i)

#Función que traduce coordenadas de pixel a índice
def translate_coords_pti(x, y):
    return y // (PADDING_SQUARE + SQUARE_SIZE), x // (PADDING_SQUARE + SQUARE_SIZE)

#Función que comprueba si las coordenadas están dentro del tablero
def valid_coords(i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

#Función que actualiza el tablero
def draw_gui():

    #Borra la pantalla
    main_screen.fill(BACKGROUND_COLOR)

    #Dibuja el tablero
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            rect = pygame.Rect(*translate_coords_itp(i, j), SQUARE_SIZE, SQUARE_SIZE)
            if selected_slot == (i, j):
                pygame.draw.rect(main_screen, LIGHT_GREY, rect)
            else:
                pygame.draw.rect(main_screen, SLOT_COLOR, rect)
            if col != -1:
                pygame.draw.circle(main_screen, PLAYER_COLORS[col], (rect.centerx, rect.centery), SQUARE_SIZE//2 -5)

    #Dibuja la barra inferior que muestra el turno o el ganador
    if win == -1:
        pygame.draw.rect(main_screen, PLAYER_COLORS[turn], pygame.Rect(PADDING_SQUARE, (PADDING_SQUARE + SQUARE_SIZE)*len(board) + PADDING_SQUARE, (SQUARE_SIZE+PADDING_SQUARE)*len(board[0]) - PADDING_SQUARE, SQUARE_SIZE))
    else:
        for ind, winner in enumerate(win):
            rect = pygame.Rect(PADDING_SQUARE + ind*((SQUARE_SIZE+PADDING_SQUARE)*len(board[0]) - PADDING_SQUARE)//len(win), (PADDING_SQUARE + SQUARE_SIZE)*len(board) + PADDING_SQUARE, ((SQUARE_SIZE+PADDING_SQUARE)*len(board[0]) - PADDING_SQUARE)//len(win), SQUARE_SIZE)
            pygame.draw.rect(main_screen, PLAYER_COLORS[winner], rect)
        text = big_font.render('Game Over', False, TEXT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = ((SQUARE_SIZE+PADDING_SQUARE)*len(board[0]) + PADDING_SQUARE)//2, (PADDING_SQUARE + SQUARE_SIZE)*len(board) + PADDING_SQUARE + SQUARE_SIZE//2
        main_screen.blit(text, text_rect)
    pygame.display.update()

#Función que resetea el juego y vuelve a la pantalla de inicio
def reset_game():
    global actual_interface, turn, win, selected_slot
    turn = 0
    win = -1
    selected_slot = None
    start_screen()

#Variables globales
actual_interface = START_INTERFACE

setup = None

bot = False
bot_depth = 0
pos_player = 0

num_rows = 1
num_columns = 1
line_size = 1
num_players = 1
num_stones = 1
misery = False
move_type = MT_NORMAL

selected_slot = None
turn = 0
win = -1

main_screen = None
board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = None, None, None, None, None, None, None

#Inicializa pygame
pygame.init()

#Definición de todos los botones del programa
button1 = pygame.Rect(PADDING*3, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//4, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button2 = pygame.Rect(PADDING*3, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button3 = pygame.Rect(PADDING*3, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)*3//4, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button4 = pygame.Rect(START_WINDOW_WIDTH//2 + PADDING, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//4, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button5 = pygame.Rect(START_WINDOW_WIDTH//2 + PADDING, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button6 = pygame.Rect(START_WINDOW_WIDTH//2 + PADDING, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)*3//4, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button_help = pygame.Rect(START_WINDOW_WIDTH - PADDING*3 - HELP_BUTTON_SIZE, PADDING*3, HELP_BUTTON_SIZE, HELP_BUTTON_SIZE)
button_go_back = pygame.Rect(START_WINDOW_WIDTH//3, START_WINDOW_HEIGHT - MEDIUM_BUTTON_HEIGHT - PADDING, MEDIUM_BUTTON_WIDHT, MEDIUM_BUTTON_HEIGHT)

button_multiplayer = pygame.Rect(START_WINDOW_WIDTH//2 - BIG_BUTTON_WIDTH//2, START_WINDOW_HEIGHT//3 - BIG_BUTTON_HEIGHT//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button_bot = pygame.Rect(START_WINDOW_WIDTH//2 - BIG_BUTTON_WIDTH//2, 2*START_WINDOW_HEIGHT//3 - BIG_BUTTON_HEIGHT//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button_dec_depth = pygame.Rect(3*START_WINDOW_WIDTH//8 - XS_BUTTON_SIZE//2, 2*START_WINDOW_HEIGHT//6 - XS_BUTTON_SIZE//2, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_depth = pygame.Rect(5*START_WINDOW_WIDTH//8 - XS_BUTTON_SIZE//2, 2*START_WINDOW_HEIGHT//6 - XS_BUTTON_SIZE//2, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_pos_player = pygame.Rect(3*START_WINDOW_WIDTH//8 - XS_BUTTON_SIZE//2, 4*START_WINDOW_HEIGHT//6 - XS_BUTTON_SIZE//2, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_pos_player = pygame.Rect(5*START_WINDOW_WIDTH//8 - XS_BUTTON_SIZE//2, 4*START_WINDOW_HEIGHT//6 - XS_BUTTON_SIZE//2, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_bot_continue = pygame.Rect(START_WINDOW_WIDTH//2 -   MEDIUM_BUTTON_WIDHT//2, 5*START_WINDOW_HEIGHT//6 - MEDIUM_BUTTON_HEIGHT//2, MEDIUM_BUTTON_WIDHT, MEDIUM_BUTTON_HEIGHT)

button_dec_num_rows = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_num_rows = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_num_columns = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_num_columns = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING + (START_WINDOW_HEIGHT - PADDING*2)//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_line_size = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*2//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_line_size = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*2//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_num_players = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*3//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_num_players = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*3//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_num_stones = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*4//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_num_stones = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*4//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_misery = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*5//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_misery = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*5//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_dec_move_type = pygame.Rect(START_WINDOW_WIDTH*2//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*6//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_inc_move_type = pygame.Rect(START_WINDOW_WIDTH - PADDING*2 - XS_BUTTON_SIZE, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*6//8, XS_BUTTON_SIZE, XS_BUTTON_SIZE)
button_custom_continue = pygame.Rect(START_WINDOW_WIDTH//3, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*7//8, MEDIUM_BUTTON_WIDHT, MEDIUM_BUTTON_HEIGHT)

#Diccionario que asocia cada interfaz con una lista de tuplas (botón, función asociada al botón)
button_master = {
    SELECT_BOT_INTERFACE: [
        (button_multiplayer, lambda: setup_game(False)),
        (button_bot, setup_bot)
    ],
    BOT_SETUP_INTERFACE: [
        (button_dec_depth, lambda: mod_bot_depth(False)),
        (button_inc_depth, lambda: mod_bot_depth(True)),
        (button_dec_pos_player, lambda: mod_pos_player(False)),
        (button_inc_pos_player, lambda: mod_pos_player(True)),
        (button_bot_continue, lambda: setup_game(True))
    ],
    CUSTOM_INTERFACE: [
        (button_dec_num_rows, lambda: mod_num_rows(False)), 
        (button_inc_num_rows, lambda: mod_num_rows(True)),
        (button_dec_num_columns, lambda: mod_num_columns(False)),
        (button_inc_num_columns, lambda: mod_num_columns(True)),
        (button_dec_line_size, lambda: mod_line_size(False)), 
        (button_inc_line_size, lambda: mod_line_size(True)),
        (button_dec_num_players, lambda: mod_num_players(False)),
        (button_inc_num_players, lambda: mod_num_players(True)),
        (button_dec_num_stones, lambda: mod_num_stones(False)),
        (button_inc_num_stones, lambda: mod_num_stones(True)),
        (button_dec_misery, mod_misery), 
        (button_inc_misery, mod_misery),
        (button_dec_move_type, lambda: mod_move_type(False)), 
        (button_inc_move_type, lambda: mod_move_type(True)),
        (button_custom_continue, custom_continue)
    ],
    GAME_INTERFACE: [],
    HELP_INTERFACE: [
        (button_go_back, start_screen)
    ],
    START_INTERFACE: [
        (button1, lambda: set_setup(0)),
        (button2, lambda: set_setup(1)),
        (button3, lambda: set_setup(2)),
        (button4, lambda: set_setup(3)),
        (button5, lambda: set_setup(4)),
        (button6, lambda: set_setup(5)),
        (button_help, help_screen)
    ]
}

#Definición de las fuentes usadas en la interfaz
big_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 25)
small_font = pygame.font.Font('freesansbold.ttf', 16)

pygame.display.set_caption("Tres en raya")

#Inicia la interfaz
start_screen()

#Bucle principal
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Si el usuario presiona el click del ratón
        elif event.type == pygame.MOUSEBUTTONDOWN:

            #Comprueba si ha presionado algún botón usando el diccionario button_master
            button_pressed = False
            for button in button_master[actual_interface]:
                if button[0].collidepoint(event.pos):
                    #Si ha presionado un botón, se ejecuta la función asociada al botón
                    button[1]()
                    #Se marca que se ha presionado un botón para evitar probelmas más adelante
                    button_pressed = True
                    break
            
            #Si no se ha presionado ningún botón y la partida está en juego
            if actual_interface == GAME_INTERFACE and not button_pressed:
                #Si es el turno del jugador y ha presionado una casilla válida
                if win == -1 and (not bot or pos_player == turn) and valid_coords(*translate_coords_pti(*event.pos)):
                    #Si se debe seleccionar una casilla
                    if setup[6] != MT_GRAVITY and bag[0] == 0 and selected_slot == None:
                        #Selecciona la casilla
                        selected_slot = translate_coords_pti(*event.pos)
                        #Solo selecciona la casilla si es válida
                        if not check_stone(turn, *selected_slot):
                            selected_slot = None
                    #Si no se debe seleccionar una casilla
                    else:
                        #Asigna el movimiento a realizar en función del tipo de movimiento
                        if setup[6] != MT_GRAVITY:
                            if selected_slot != None:
                                m = (*selected_slot, *translate_coords_pti(*event.pos))
                            else:
                                m = translate_coords_pti(*event.pos)
                        else:
                            m = (translate_coords_pti(*event.pos)[1],)

                        #Si el movimiento es válido, lo realiza
                        if m != None and m in possible_moves(turn):                            
                            last_i, last_j = player_move(m, turn)
                            m = None
                            #Comprueba si ha acabado el juego tras el movimiento
                            win = end_checker(last_i, last_j)
                        #Desselecciona la casilla (si es que se ha seleccionado)
                        selected_slot = None
                #Si la partida ya ha acabado, reinicia el juego al hacer click
                elif win != -1:
                    reset_game()

    #Si la partida está en juego
    if actual_interface == GAME_INTERFACE:
        #Comprobará el turno
        turn = num_players - bag[1]
        #Si se está jugando contra el bot y es el turno del bot, realiza un movimiento
        if win == -1 and bot and pos_player != turn:
            draw_gui()
            last_i, last_j = bot_move(turn, bot_depth)
            win = end_checker(last_i, last_j)
        draw_gui()
    
    #Actualiza la pantalla
    pygame.display.update()