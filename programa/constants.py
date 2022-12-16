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
- El número de filas, el número de columnas, número de piezas de un mismo jugador que haze raya i el número de jugadores tienen que ser números enteros positivos i diferentes de zero\n\
- Si el número de piedras és -1 las dos siguientes indicaciones no se tienen que seguir\n\
- El número de piedras tiene que ser más grande o igual que el número de piezas de un mismo jugador que hace raya\n\
- El número de piedras multiplicado por el número de jugadores tiene que ser más pequeño o igual que el número de filas por el número de columnas menos 1\n\
Ej: 7 7 7 3 8 M A"
VARIANT_SETUPS = ((3, 3, 3, 2, 3, False, MT_NORMAL), \
                    (3, 3, 3, 2, 4, True, MT_NORMAL), \
                    (3, 3, 3, 2, 3, False, MT_ADJACENT), \
                    (3, 3, 3, 2, 4, True, MT_ADJACENT), \
                    (6, 7, 4, 2, -1, False, MT_GRAVITY))




