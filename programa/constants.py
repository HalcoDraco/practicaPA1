MT_NORMAL = "normal"
MT_ADJACENT = "adjacent"
MT_GRAVITY = "gravity"

variants = ("Tres en raya clásico", "Tres en raya clásico misery", "Tres en raya adyacente", "Tres en raya adyacente misery", "Cuatro en raya", "Custom")
variant_descriptions = ("Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya gana", \
    "Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya pierde", \
    "Tablero de 3x3, 3 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya gana.\nLas piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\nSi un jugador llega a una situación en la que no puede mover ninguna pidra, pierde.", \
    "Tablero de 3x3, 4 piedras por jugador, 2 jugadores.\nEl primero en hacer 3 en raya pierde.\nLas piedras solo se pueden mover a posiciones adyacentes en horizontal o vertical.\nSi un jugador llega a una situación en la que no puede mover ninguna pidra, pierde.", \
    "Tablero de 6x7, sin límite de piedras, 2 jugadores.\nEl primero en hacer 4 en raya gana.\nLas piedras solo se pueden colocar en una de las 7 columnas, y caeran por gravedad hasta topar con otra piedra o llegar al fondo del tablero.", \
    "Modo de juego completamente customizable. Se puede personalizar lo siguiente:\n\tLas dimensiones del tablero\n\tEl número de jugadores\n\tEl número de piedras por jugador\n\tEl tamaño n de la raya para hacer n en raya\n\tSi el juego es misery o no\n\tSi la forma de mover las piezas es clásica, adyacente o por gravedad")
variant_setups = ((3, 3, 3, 2, 3, False, MT_NORMAL), \
                    (3, 3, 3, 2, 4, True, MT_NORMAL), \
                    (3, 3, 3, 2, 3, False, MT_ADJACENT), \
                    (3, 3, 3, 2, 4, True, MT_ADJACENT), \
                    (6, 7, 4, 2, -1, False, MT_GRAVITY))


