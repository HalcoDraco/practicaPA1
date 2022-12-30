import pygame
from constants import *
from abs_board import board_setup, custom_board_checker

def start_screen():
    text = font.render('Escoge el modo de juego:', True, (0, 0, 0), None)
    help = font.render('?', True, (0, 0, 0), None)
    num1_txt = font.render('1', True, (0, 0, 0), None)
    num2_txt = font.render('2', True, (0, 0, 0), None)
    num3_txt = font.render('3', True, (0, 0, 0), None)
    num4_txt = font.render('4', True, (0, 0, 0), None)
    num5_txt = font.render('5', True, (0, 0, 0), None)
    num6_txt = font.render('6', True, (0, 0, 0), None)

    textRect = text.get_rect()
    helpRect = text.get_rect()
    num1_txt_Rect = num1_txt.get_rect()
    num2_txt_Rect = num2_txt.get_rect()
    num3_txt_Rect = num3_txt.get_rect()
    num4_txt_Rect = num4_txt.get_rect()
    num5_txt_Rect = num5_txt.get_rect()
    num6_txt_Rect = num6_txt.get_rect()

    textRect.center = (270, 70)
    helpRect.center = (870, 70)
    num1_txt_Rect.center = (210, 185)
    num2_txt_Rect.center = (210, 295)
    num3_txt_Rect.center = (210, 405)
    num4_txt_Rect.center = (540, 185)
    num5_txt_Rect.center = (540, 295)
    num6_txt_Rect.center = (540, 405)

    pygame.draw.rect(main_screen, GREY, button1)
    pygame.draw.rect(main_screen, GREY, button2)
    pygame.draw.rect(main_screen, GREY, button3)
    pygame.draw.rect(main_screen, GREY, button4)
    pygame.draw.rect(main_screen, GREY, button5)
    pygame.draw.rect(main_screen, GREY, button6)
    pygame.draw.rect(main_screen, LIGHT_GREY, button_help)
    main_screen.blit(text, textRect)
    main_screen.blit(help, helpRect)
    main_screen.blit(num1_txt, num1_txt_Rect)
    main_screen.blit(num2_txt, num2_txt_Rect)
    main_screen.blit(num3_txt, num3_txt_Rect)
    main_screen.blit(num4_txt, num4_txt_Rect)
    main_screen.blit(num5_txt, num5_txt_Rect)
    main_screen.blit(num6_txt, num6_txt_Rect)

def set_setup(num):
    global setup, board, check_stone, possible_moves, player_move, bot_move, end_checker, bag, num_players
    if num != 5:
        setup = VARIANT_SETUPS[num]
        board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = board_setup(*setup)
        num_players = setup[3]
    else:
        pass
    
    select_bot_multi()

def select_bot_multi():
    global main_screen, actual_interface
    main_screen.fill(BACKGROUND_COLOR)
    actual_interface = SELECT_BOT_INTERFACE
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_multiplayer)
    pygame.draw.rect(main_screen, BUTTON_COLOR, button_bot)
    text = font.render('Multiplayer', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_multiplayer.centerx, button_multiplayer.centery)))
    text = font.render('Bot', False, TEXT_COLOR)
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
    text = font.render('Dificultad del bot', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, START_WINDOW_HEIGHT//6)))
    text = font.render('Turno del jugador', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 3*START_WINDOW_HEIGHT//6)))
    text = font.render('-', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_dec_depth.centerx, button_dec_depth.centery)))
    main_screen.blit(text, text.get_rect(center = (button_dec_pos_player.centerx, button_dec_pos_player.centery)))
    text = font.render('+', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_inc_depth.centerx, button_inc_depth.centery)))
    main_screen.blit(text, text.get_rect(center = (button_inc_pos_player.centerx, button_inc_pos_player.centery)))
    text = font.render('Continuar', False, TEXT_COLOR)
    main_screen.blit(text, text.get_rect(center = (button_bot_continue.centerx, button_bot_continue.centery)))
    update_values()

def update_values():
    global main_screen
    text = font.render(str(bot_depth), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 2*START_WINDOW_HEIGHT//6)))
    text = font.render(str(pos_player+1), True, TEXT_COLOR, BACKGROUND_COLOR)
    main_screen.blit(text, text.get_rect(center = (START_WINDOW_WIDTH//2, 4*START_WINDOW_HEIGHT//6)))

def dec_depth():
    global bot_depth
    if bot_depth > 0:
        bot_depth -= 1
        update_values()

def inc_depth():
    global bot_depth
    if bot_depth < 3:
        bot_depth += 1
        update_values()

def dec_pos_player():
    global pos_player
    if pos_player > 0:
        pos_player -= 1
        update_values()
    
def inc_pos_player():
    global pos_player
    if pos_player < num_players - 1:
        pos_player += 1
        update_values()

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
    main_screen = pygame.display.set_mode((len(board[0])*(PADDING + SQUARE_SIZE) + PADDING, len(board)*(PADDING + SQUARE_SIZE) + 2*PADDING + 100))
    actual_interface = GAME_INTERFACE
    draw_board()

# index to pixel
def translate_coords_itp(i, j):
    return (PADDING + (PADDING + SQUARE_SIZE)*j, PADDING + (PADDING + SQUARE_SIZE)*i)

# pixel to index
def translate_coords_pti(x, y):
    return y // (PADDING + SQUARE_SIZE), x // (PADDING + SQUARE_SIZE)

# check if index coords are valid
def valid_coords(i, j):
    return 0 <= i < len(board) and 0 <= j < len(board[0])

def draw_board():
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
            rect = pygame.Rect(PADDING + ind*((SQUARE_SIZE+PADDING)*len(board[0]) - PADDING)/len(win), (PADDING + SQUARE_SIZE)*len(board) + PADDING, ((SQUARE_SIZE+PADDING)*len(board[0]) - PADDING)/len(win), SQUARE_SIZE)
            pygame.draw.rect(main_screen, PLAYER_COLORS[winner], rect)


actual_interface = START_INTERFACE

setup = ()


bot = False
bot_depth = 0
pos_player = 0


selected_slot = None
turn = 0
win = -1

pygame.init()

main_screen = pygame.display.set_mode((START_WINDOW_WIDTH, START_WINDOW_HEIGHT))
main_screen.fill(BACKGROUND_COLOR)

button1 = pygame.Rect(60, 150, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button2 = pygame.Rect(60, 260, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button3 = pygame.Rect(60, 370, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button4 = pygame.Rect(390, 150, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button5 = pygame.Rect(390, 260, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button6 = pygame.Rect(390, 370, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button_help = pygame.Rect(655, 45, 50, 50)

button_multiplayer = pygame.Rect(START_WINDOW_WIDTH//2 - BIG_BUTTON_WIDTH//2, START_WINDOW_HEIGHT//3 - BIG_BUTTON_HEIGHT//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button_bot = pygame.Rect(START_WINDOW_WIDTH//2 - BIG_BUTTON_WIDTH//2, 2*START_WINDOW_HEIGHT//3 - BIG_BUTTON_HEIGHT//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)
button_dec_depth = pygame.Rect(3*START_WINDOW_WIDTH//8 - SMALL_BUTTON_WIDTH//2, 2*START_WINDOW_HEIGHT//6 - SMALL_BUTTON_HEIGHT//2, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
button_inc_depth = pygame.Rect(5*START_WINDOW_WIDTH//8 - SMALL_BUTTON_WIDTH//2, 2*START_WINDOW_HEIGHT//6 - SMALL_BUTTON_HEIGHT//2, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
button_dec_pos_player = pygame.Rect(3*START_WINDOW_WIDTH//8 - SMALL_BUTTON_WIDTH//2, 4*START_WINDOW_HEIGHT//6 - SMALL_BUTTON_HEIGHT//2, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
button_inc_pos_player = pygame.Rect(5*START_WINDOW_WIDTH//8 - SMALL_BUTTON_WIDTH//2, 4*START_WINDOW_HEIGHT//6 - SMALL_BUTTON_HEIGHT//2, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT)
button_bot_continue = pygame.Rect(START_WINDOW_WIDTH//2 - BIG_BUTTON_WIDTH//2, 5*START_WINDOW_HEIGHT//6 - BIG_BUTTON_HEIGHT//2, BIG_BUTTON_WIDTH, BIG_BUTTON_HEIGHT)

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
    GAME_INTERFACE: [],
    START_INTERFACE: [
        (button1, lambda: set_setup(0)),
        (button2, lambda: set_setup(1)),
        (button3, lambda: set_setup(2)),
        (button4, lambda: set_setup(3)),
        (button5, lambda: set_setup(4)),
        (button6, lambda: set_setup(5))
    ]
}

font = pygame.font.Font('freesansbold.ttf', 32)

start_screen()
board, check_stone, possible_moves, player_move, bot_move, end_checker, bag = (0, 0, 0, 0, 0, 0, 0)
num_players = 0

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in button_master[actual_interface]:
                if button[0].collidepoint(event.pos):
                    button[1]()
            #comprobar qué main_screen está en pantalla
            if actual_interface == GAME_INTERFACE:
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
                            win = end_checker(last_i, last_j)
                        selected_slot = None

    if actual_interface == GAME_INTERFACE:
        turn = num_players - bag[1]
        if win == -1 and bot and pos_player != turn:
            draw_board()
            last_i, last_j = bot_move(turn, bot_depth)
            win = end_checker(last_i, last_j)

        draw_board()
    
    pygame.display.update()