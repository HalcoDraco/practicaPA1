#Tipos de movimiento
MT_NORMAL = "normal"
MT_ADJACENT = "adjacent"
MT_GRAVITY = "gravity"

#Títulos de las variantes
VARIANTS = ("Tres en raya clásico", "Tres en raya clásico misery", "Tres en raya adyacente", "Tres en raya adyacente misery", "Cuatro en raya", "Custom")

#Descripciones de las variantes
VARIANT_DESCRIPTIONS = ("Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya gana", \
    "Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya pierde", \
    "Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya gana.\nLas piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\nSi un jugador llega a una situación en la que no puede mover ninguna piedra, pierde.", \
    "Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya pierde.\nLas piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\nSi un jugador llega a una situación en la que no puede mover ninguna piedra, pierde.", \
    "Tablero de 6x7, sin límite de piedras, 2 jugadores.\nEl primero en hacer 4 en raya gana.\nLas piedras solo se pueden colocar en una de las 7 columnas, y caerán por gravedad hasta topar con otra piedra o llegar al fondo del tablero.", \
    "Modo de juego completamente customizable. Se puede personalizar lo siguiente:\n\tLas dimensiones del tablero\n\tEl número de jugadores\n\tEl número de piedras por jugador\n\tEl tamaño n de la raya para hacer n en raya\n\tSi el juego es misery o no\n\tSi la forma de mover las piezas es clásica, adyacente o por gravedad")

#Mensajes de la variante custom
CUSTOM_DESCRIPTION = ("Introduce los parámetros de tu elección para acceder a la variante custom siguiendo este patrón:",
"<número de filas>\n<número de columnas>\n<número de piezas de un mismo jugador que hace raya>\n<número de jugadores>\n<número de piedras>\n<si es la variante misery>\n<tipo de movimiento>",
"A la hora de introducir los parámetros debes tener las siguientes indicaciones presentes:",
"- Pon 'M' si quieres que la variante sea misery y 'NM' si quieres que no lo sea\n\
- Pon 'N' si quieres que el movimiento sea normal, 'A' si quieres que sea adyacente y 'G' si quieres que sea con gravedad\n\
- Pon -1 si quieres que el número de piedras sea infinito\n\
- El número de jugadores tiene que ser más pequeño o igual a 10 y mayor o igual a dos\n\
- El número de piezas de un mismo jugador que hace raya tiene que ser menor o igual al máximo del número de filas y el número de columnas\n\
- El número de filas, el número de columnas, número de piezas de un mismo jugador que hace raya y el número de jugadores tienen que ser números enteros positivos y diferentes de zero\n\
- Si el número de piedras es -1 las dos siguientes indicaciones no se tienen que seguir\n\
- El número de piedras tiene que ser más grande o igual que el número de piezas de un mismo jugador que hace raya\n\
- El número de piedras multiplicado por el número de jugadores tiene que ser más pequeño o igual que el número de filas por el número de columnas menos 1",
"Ej: 7 7 7 3 8 M A")

#Manual de juego del tres en raya con pygame
GAME_DESCRIPTION = ("Normal:\n  Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\n  El primero en hacer 3 en raya gana\n\n\
Misery:\n  Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\n  El primero en hacer 3 en raya pierde\n\n\
Adyacente:\n  Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\n  El primero en hacer 3 en raya gana.\n  Las piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\n  Si un jugador llega a una situación en la que no puede mover ninguna piedra, pierde.\n\n\
Misery ady:\n  Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\n  El primero en hacer 3 en raya pierde.\n  Las piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\n  Si un jugador llega a una situación en la que no puede mover ninguna piedra, pierde.\n\n\
4 en raya:\n  Tablero de 6x7, sin límite de piedras, 2 jugadores.\n  El primero en hacer 4 en raya gana.\n  Las piedras solo se pueden colocar en una de las 7 columnas, y caerán por gravedad hasta topar con otra piedra\n  o llegar al fondo del tablero.", \
"Custom:\n  Modo de juego completamente customizable. Se puede personalizar lo siguiente:\n   - Las dimensiones del tablero\n   - El número de jugadores\n   - El número de piedras por jugador\n   - El tamaño n de la raya para hacer n en raya\n   - Si el juego es misery o no\n   - Si la forma de mover las piezas es clásica, adyacente o por gravedad\n\n\
Funcionamiento de custom:\n  El tablero mínimo es de 2x2.\n  El tamaño de línea puede ser desde 1 hasta el máximo de filas o columnas.\n  El número de jugadores puede ser desde 2 hasta 10\n  Escoge -1 número de piedras si quieres tener piedras infinitas.\n  El número de piedras por jugador, si no es -1, tiene que ser mayor o igual que el tamaño de línea.\n  El total de piedras, si el número de piedras no es -1, en el tablero tiene que ser menor que el número de casillas.\n\n\
Funcionamiento del bot:\n  El nivel de dificultad determina la profundidad de búsqueda del bot. La búsqueda tiene una complejidad\n  exponencial, por lo que se debe ajustar este valor con mucho cuidado.\n  La cantidad de comprobaciones que hace, viene determinada, más o menos por la fórmula siguiente:\n  num_movimientos_posibles ^ (1 + profundidad * num_jugadores)\n  Sé prudente escogiendo el nivel o tus partidas no acabarán nunca.")

#Variantes predefinidas
VARIANT_SETUPS = ((3, 3, 3, 2, 3, False, MT_NORMAL), \
                    (3, 3, 3, 2, 4, True, MT_NORMAL), \
                    (3, 3, 3, 2, 3, False, MT_ADJACENT), \
                    (3, 3, 3, 2, 4, True, MT_ADJACENT), \
                    (6, 7, 4, 2, -1, False, MT_GRAVITY))

#Colores
WHITE = (255,255,255)
BLACK = (0, 0, 0)
LIGHT_GREY = (190, 190, 190)
GREY = (150, 150, 150)
RED = (255, 0, 0)

REDISH = (212,  17,  89)
BLUE = (26, 133, 255)
GREEN = (4, 201, 63)
YELLOW = (244, 252, 3)
ORANGE = (252, 186, 3)
PURPLE = (159, 22, 184)
CYAN = (10, 250, 218)
PINK = (250, 87, 177)
LIGHT_PURPLE = (232, 119, 252)
LIGHT_BLUE = (115, 178, 250)
LIGHT_GREEN = (2, 250, 77)

BACKGROUND_COLOR = LIGHT_GREY
TEXT_COLOR = BLACK
BUTTON_COLOR = GREY
SLOT_COLOR = WHITE

#Colores de los jugadores
PLAYER_COLORS = {0: REDISH, 1: BLUE, 2: GREEN, 3: YELLOW, 4: ORANGE, 5: PURPLE, 6: CYAN, 7: PINK, 8: LIGHT_PURPLE, 9: LIGHT_BLUE, 10: LIGHT_GREEN}

#Tamaños
SQUARE_SIZE = 70
PADDING_SQUARE = 10
PADDING = 20

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
HELP_INTERFACE = "help"





