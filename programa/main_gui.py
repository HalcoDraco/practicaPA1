import pygame
from constants import *
from abs_board import board_setup, custom_board_checker

def start_screen():
    global main_screen
    main_screen = pygame.display.set_mode((START_WINDOW_WIDTH, START_WINDOW_HEIGHT))
    main_screen.fill(BACKGROUND_COLOR)

    text = big_font.render('Escoge el modo de juego:', False, TEXT_COLOR)
    help = big_font.render('?', False, TEXT_COLOR)
    num1_txt = big_font.render('Normal', False, TEXT_COLOR)
    num2_txt = big_font.render('Misery', False, TEXT_COLOR)
    num3_txt = big_font.render('Adyacente', False, TEXT_COLOR)
    num4_txt = big_font.render('Misery ady', False, TEXT_COLOR)
    num5_txt = big_font.render('4 en raya', False, TEXT_COLOR)
    num6_txt = big_font.render('Custom', False, TEXT_COLOR)

    pygame.draw.rect(main_screen, GREY, button1)
    pygame.draw.rect(main_screen, GREY, button2)
    pygame.draw.rect(main_screen, GREY, button3)
    pygame.draw.rect(main_screen, GREY, button4)
    pygame.draw.rect(main_screen, GREY, button5)
    pygame.draw.rect(main_screen, GREY, button6)
    pygame.draw.rect(main_screen, LIGHT_GREY, button_help)

    main_screen.blit(text, (PADDING*3, PADDING*3))
    main_screen.blit(help, help.get_rect(center = (START_WINDOW_WIDTH - PADDING*3 - HELP_BUTTON_SIZE//2, PADDING*3 + HELP_BUTTON_SIZE//2)))
    main_screen.blit(num1_txt, num1_txt.get_rect(center = (PADDING*3 + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//4 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num2_txt, num2_txt.get_rect(center = (PADDING*3 + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//2 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num3_txt, num3_txt.get_rect(center = (PADDING*3 + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)*3//4 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num4_txt, num4_txt.get_rect(center = (START_WINDOW_WIDTH//2 + PADDING + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//4 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num5_txt, num5_txt.get_rect(center = (START_WINDOW_WIDTH//2 + PADDING + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)//2 + BIG_BUTTON_HEIGHT//2)))
    main_screen.blit(num6_txt, num6_txt.get_rect(center = (START_WINDOW_WIDTH//2 + PADDING + BIG_BUTTON_WIDTH//2, PADDING*3 + (START_WINDOW_HEIGHT - PADDING*6)*3//4 + BIG_BUTTON_HEIGHT//2)))
    
def custom_board():
    global main_screen, actual_interface
    main_screen.fill(BACKGROUND_COLOR)

    actual_interface = CUSTOM_INTERFACE

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

    update_values_custom()

def multi_line_renderer(text, font, color, surface, x, y, line_spacing = 0):
    lines = text.splitlines()
    for line in lines:
        surface.blit(font.render(line, False, color), (x, y))
        y += font.get_linesize() + line_spacing

def help_screen():
    global main_screen, actual_interface
    main_screen.fill(BACKGROUND_COLOR)
    actual_interface = HELP_INTERFACE

    multi_line_renderer(CUSTOM_DESCRIPTION[3], medium_font, TEXT_COLOR, main_screen, PADDING, PADDING)

    pygame.draw.rect(main_screen, GREY, button_go_back)
    go_back_txt = big_font.render('Volver', False, TEXT_COLOR)
    main_screen.blit(go_back_txt, go_back_txt.get_rect(center = (START_WINDOW_WIDTH//2, START_WINDOW_HEIGHT - MEDIUM_BUTTON_HEIGHT//2 - PADDING)))
    
def set_setup(num):
    global setup, board, check_stone, possible_moves, player_move, bot_move, end_checker, bag, num_players
    if num != 5:
        setup = VARIANT_SETUPS[num]
        board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = board_setup(*setup)
        num_players = setup[3]
        select_bot_multi()
    else:
        custom_board()
    
def select_bot_multi():
    global main_screen, actual_interface
    main_screen.fill(BACKGROUND_COLOR)
    actual_interface = SELECT_BOT_INTERFACE
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_multiplayer)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_bot)
    text = big_font.render('Multiplayer', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_multiplayer.centerx, button_multiplayer.centery)))
    text = big_font.render('Bot', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_bot.centerx, button_bot.centery)))

def setup_bot():
    global main_screen, actual_interface
    main_screen.fill(BACKGROUND_COLOR)
    actual_interface = BOT_SETUP_INTERFACE
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
    update_values_bot()

def update_values_bot():
    global main_screen
    text = big_font.render(str(bot_depth), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 2*START_WINDOW_HEIGHT//6)))
    text = big_font.render(str(pos_player+1), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 4*START_WINDOW_HEIGHT//6)))

def update_values_custom():
    global main_screen
    rectangulo = pygame.Rect(0, 0, 100, START_WINDOW_HEIGHT)
    rectangulo.centerx = START_WINDOW_WIDTH*5//6 - PADDING//2
    pygame.draw.rect(main_screen, BACKGROUND_COLOR, rectangulo)
    pygame.draw.rect(main_screen, BACKGROUND_COLOR, pygame.Rect(START_WINDOW_WIDTH*2//3 + XS_BUTTON_SIZE//2, PADDING + (START_WINDOW_HEIGHT - PADDING*2)*7//8 + MEDIUM_BUTTON_HEIGHT//4, MEDIUM_BUTTON_WIDHT, MEDIUM_BUTTON_HEIGHT))

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

def go_back():
    global actual_interface
    actual_interface = START_INTERFACE
    start_screen()

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

def dec_depth():
    global bot_depth
    if bot_depth > 0:
        bot_depth -= 1
        update_values_bot()

def inc_depth():
    global bot_depth
    if bot_depth < 3:
        bot_depth += 1
        update_values_bot()

def dec_pos_player():
    global pos_player
    if pos_player > 0:
        pos_player -= 1
        update_values_bot()
    
def inc_pos_player():
    global pos_player
    if pos_player < num_players - 1:
        pos_player += 1
        update_values_bot()

def start_multiplayer():
    global bot
    bot = False
    setup_game()

def start_bot():
    global bot
    bot = True
    setup_game()

def setup_game():
    global main_screen, actual_interface
    main_screen = pygame.display.set_mode((len(board[0])*(PADDING + SQUARE_SIZE) + PADDING, len(board)*(PADDING + SQUARE_SIZE) + 2*PADDING + SQUARE_SIZE))
    draw_gui()
    actual_interface = GAME_INTERFACE
    
# index to pixel
def translate_coords_itp(i, j):
    return (PADDING + (PADDING + SQUARE_SIZE)*j, PADDING + (PADDING + SQUARE_SIZE)*i)

# pixel to index
def translate_coords_pti(x, y):
    return y // (PADDING + SQUARE_SIZE), x // (PADDING + SQUARE_SIZE)

# check if index coords are valid
def valid_coords(i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def draw_gui():
    main_screen.fill(BACKGROUND_COLOR)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            rect = pygame.Rect(*translate_coords_itp(i, j), SQUARE_SIZE, SQUARE_SIZE)
            if selected_slot == (i, j):
                pygame.draw.rect(main_screen, LIGHT_GREY, rect)
            else:
                pygame.draw.rect(main_screen, SLOT_COLOR, rect)
            if col != -1:
                pygame.draw.circle(main_screen, PLAYER_COLORS[col], (rect.centerx, rect.centery), SQUARE_SIZE//2 -5)
    if win == -1:
        pygame.draw.rect(main_screen, PLAYER_COLORS[turn], pygame.Rect(PADDING, (PADDING + SQUARE_SIZE)*len(board) + PADDING, (SQUARE_SIZE+PADDING)*len(board[0]) - PADDING, SQUARE_SIZE))
    else:
        for ind, winner in enumerate(win):
            rect = pygame.Rect(PADDING + ind*((SQUARE_SIZE+PADDING)*len(board[0]) - PADDING)//len(win), (PADDING + SQUARE_SIZE)*len(board) + PADDING, ((SQUARE_SIZE+PADDING)*len(board[0]) - PADDING)//len(win), SQUARE_SIZE)
            pygame.draw.rect(main_screen, PLAYER_COLORS[winner], rect)
        text = big_font.render('Game Over', False, TEXT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = ((SQUARE_SIZE+PADDING)*len(board[0]) + PADDING)//2, (PADDING + SQUARE_SIZE)*len(board) + PADDING + SQUARE_SIZE//2
        main_screen.blit(text, text_rect)
    pygame.display.update()

def reset_game():
    global actual_interface, turn, win, selected_slot
    actual_interface = START_INTERFACE
    turn = 0
    win = -1
    selected_slot = None
    start_screen()


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

pygame.init()

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

button_master = {
    SELECT_BOT_INTERFACE: [
        (button_multiplayer, start_multiplayer),
        (button_bot, setup_bot)
    ],
    BOT_SETUP_INTERFACE: [
        (button_dec_depth, dec_depth),
        (button_inc_depth, inc_depth),
        (button_dec_pos_player, dec_pos_player),
        (button_inc_pos_player, inc_pos_player),
        (button_bot_continue, start_bot)
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
        (button_go_back, go_back)
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

big_font = pygame.font.Font('freesansbold.ttf', 32)
medium_font = pygame.font.Font('freesansbold.ttf', 25)
small_font = pygame.font.Font('freesansbold.ttf', 16)

main_screen = None
pygame.display.set_caption("Tres en raya")

start_screen()

board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = None, None, None, None, None, None, None

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = False
            for button in button_master[actual_interface]:
                if button[0].collidepoint(event.pos):
                    button[1]()
                    button_pressed = True
                    break

            if actual_interface == GAME_INTERFACE and not button_pressed:
                if win == -1 and (not bot or pos_player == turn) and valid_coords(*translate_coords_pti(*event.pos)):
                    if setup[6] != MT_GRAVITY and bag[0] == 0 and selected_slot == None:
                        selected_slot = translate_coords_pti(*event.pos)
                        if not check_stone(turn, *selected_slot):
                            selected_slot = None
                    else:
                        if setup[6] != MT_GRAVITY:
                            if selected_slot != None:
                                m = (*selected_slot, *translate_coords_pti(*event.pos))
                            else:
                                m = translate_coords_pti(*event.pos)
                        else:
                            m = (translate_coords_pti(*event.pos)[1],)
                    
                        if m != None and m in possible_moves(turn):                            
                            last_i, last_j = player_move(m, turn)
                            m = None
                            win = end_checker(last_i, last_j)
                        selected_slot = None
                elif win != -1:
                    actual_interface = START_INTERFACE
                    reset_game()

    if actual_interface == GAME_INTERFACE:
        turn = num_players - bag[1]
        if win == -1 and bot and pos_player != turn:
            draw_gui()
            last_i, last_j = bot_move(turn, bot_depth)
            win = end_checker(last_i, last_j)

        draw_gui()
    
    pygame.display.update()