#Move types
MT_NORMAL = "normal"
MT_ADJACENT = "adjacent"
MT_GRAVITY = "gravity"

#Variants
VARIANTS = ("Tres en raya clásico", "Tres en raya clásico misery", "Tres en raya adyacente", "Tres en raya adyacente misery", "Cuatro en raya", "Custom")
VARIANT_DESCRIPTIONS = ("Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya gana", \
    "Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya pierde", \
    "Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya gana.\nLas piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\nSi un jugador llega a una situación en la que no puede mover ninguna pidra, pierde.", \
    "Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya pierde.\nLas piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\nSi un jugador llega a una situación en la que no puede mover ninguna pidra, pierde.", \
    "Tablero de 6x7, sin límite de piedras, 2 jugadores.\nEl primero en hacer 4 en raya gana.\nLas piedras solo se pueden colocar en una de las 7 columnas, y caeran por gravedad hasta topar con otra piedra o llegar al fondo del tablero.", \
    "Modo de juego completamente customizable. Se puede personalizar lo siguiente:\n\tLas dimensiones del tablero\n\tEl número de jugadores\n\tEl número de piedras por jugador\n\tEl tamaño n de la raya para hacer n en raya\n\tSi el juego es misery o no\n\tSi la forma de mover las piezas es clásica, adyacente o por gravedad")
CUSTOM_DESCRIPTION = "Introduce los parámetros de tu elección para acceder a la variante custom siguiendo este patrón:\n\
<número de filas> <número de columnas> <número de piezas de un mismo jugador que haze raya> <número de jugadores> <número de piedras> <si es la variante misery> <tipo de movimiento>\n\
A la hora de introducir los parámetros debes tener los siguientes indicaciones presentes:\n\
- Pon 'M' si quieres que la variante sea misery y 'NM' si quieres que no lo sea\n\
- Pon 'N' si quieres que el movimiento sea normal, 'A' si quieres que sea adyacente y 'G' si quieres que sea con gravedad\n\
- Pon -1 si quieres que el número de piedras sea infinito\n\
- El número de jugadores tiene que ser más pequeño o igual a 10\n\
- El número de piezas de un mismo jugador que haze raya tiene que ser inferior o igual que el número de filas o el número de columnas\n\
- El número de filas, el número de columnas, número de piezas de un mismo jugador que hace raya i el número de jugadores tienen que ser números enteros positivos i diferentes de zero\n\
- Si el número de piedras és -1 las dos siguientes indicaciones no se tienen que seguir\n\
- El número de piedras tiene que ser más grande o igual que el número de piezas de un mismo jugador que hace raya\n\
- El número de piedras multiplicado por el número de jugadores tiene que ser más pequeño o igual que el número de filas por el número de columnas menos 1\n\
Ej: 7 7 7 3 8 M A"
VARIANT_SETUPS = ((3, 3, 3, 2, 3, False, MT_NORMAL), \
                    (3, 3, 3, 2, 4, True, MT_NORMAL), \
                    (3, 3, 3, 2, 3, False, MT_ADJACENT), \
                    (3, 3, 3, 2, 4, True, MT_ADJACENT), \
                    (6, 7, 4, 2, -1, False, MT_GRAVITY))

#Colors
WHITE = (255,255,255)
BLACK = (0, 0, 0)
REDISH = (212,  17,  89)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (26, 133, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_GREY = (190, 190, 190)
GREY = (150, 150, 150)

BACKGROUND_COLOR = LIGHT_GREY
TEXT_COLOR = BLACK
BUTTON_COLOR = GREY
SLOT_COLOR = WHITE

#Player color dictionary
PLAYER_COLORS = {0: REDISH, 1: BLUE, 2: GREEN, 3: YELLOW, 4: ORANGE, 5: PURPLE, 6: CYAN, 7: PINK, 8: BROWN, 9: LIGHT_BLUE, 10: LIGHT_GREEN}

#Sizes
SQUARE_SIZE = 100
PADDING = 20
LITTLE_PADDING = 10

START_WINDOW_WIDTH = 750
START_WINDOW_HEIGHT = 500

BIG_BUTTON_WIDTH = 300
BIG_BUTTON_HEIGHT = 70

SMALL_BUTTON_WIDTH = 60
SMALL_BUTTON_HEIGHT = 50

MEDIUM_BUTTON_WIDHT = 250
MEDIUM_BUTTON_HEIGHT = 50

XS_BUTTON_SIZE = 35

HELP_BUTTON_SIZE = SMALL_BUTTON_HEIGHT

#Interfaces
START_INTERFACE = "start"
GAME_INTERFACE = "game"
SELECT_BOT_INTERFACE = "select_bot"
BOT_SETUP_INTERFACE = "bot_setup"
CUSTOM_INTERFACE = "custom"





