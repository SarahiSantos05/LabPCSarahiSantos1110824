# Define el tamaño del tablero de ajedrez
TAMANODELTABLERO = 8
# Lista de piezas válidas en el juego
PIEZAS_VALIDAS = ['peon', 'caballo', 'alfil', 'torre', 'dama', 'rey']

def piezas_a_validar(tipo):
    # Valida si el tipo de pieza ingresado está en la lista de piezas válidas
    return tipo.lower() in PIEZAS_VALIDAS

def la_posicion_es_valida(posicion):
    # Define las letras y números válidos para las posiciones en el tablero
    letras_que_son_validas = 'abcdefgh'
    numeros_que_son_validos = '12345678'
    # Verifica que la longitud de la entrada sea 2 (letra y número)
    if len(posicion) != 2:
        return False
    letra, numero = posicion[0].lower(), posicion[1]
    # Valida que la letra y el número estén dentro de los rangos permitidos
    return letra in letras_que_son_validas and numero in numeros_que_son_validos

def color_a_validar(color):
    # Valida que el color ingresado sea blanco o negro
    return color.lower() in ['blanco', 'negro']

def tablero_juego(tablero):
    # Imprime el tablero con líneas para representar las casillas
    linea_horizontal = '  »' + ('---»' * TAMANODELTABLERO)
    print('   ' + '   '.join('ABCDEFGH'))
    print(linea_horizontal)
    for i in range(len(tablero)):
        print(f"{8 - i} |", end='')
        for j in range(len(tablero[i])):
            casilla = tablero[i][j]
            print(f" {casilla if casilla else ' '} |", end='')
        print()
        print(linea_horizontal)

def usuario_ingresar_la_pieza(es_caballo=False):
    # Función para ingresar una pieza en el tablero, permitiendo configuración específica para el caballo
    if es_caballo:
        print("Configura el caballo a observar")
        tipo = 'CN'
    else:
        tipo = input("Añade el tipo de pieza | peon, caballo, alfil, torre, dama, rey |: ").lower()
        while not piezas_a_validar(tipo):
            print("La pieza ingresada es incorrecta.")
            tipo = input("Añade el tipo de pieza | peon, caballo, alfil, torre, dama, rey |: ").lower()
        tipo = tipo[0].upper() + 'N'
    color = input("Qué color será la pieza? (blanco o negro): ")
    while not color_a_validar(color):
        print("El color ingresado es incorrecto.")
        color = input("Qué color será la pieza? (blanco o negro): ")
    posicion = input("Agrega la posición de la pieza, del 1-8, y de a-h | ejemplo: a1, e4, f8 |: ")
    while not la_posicion_es_valida(posicion):
        print("La posición ingresada no es correcta.")
        posicion = input("Ingresá una posición correcta | por ejemplo, a1, e4, f8 |: ")
    return tipo, color[0].upper(), posicion

def que_movimientos_del_caballo_hay(posicion, tablero, color):
    movimientos = []
    desplazamientos_x = [2, 1, -1, -2, -2, -1, 1, 2]
    desplazamientos_y = [1, 2, 2, 1, -1, -2, -2, -1]
    letra, numero = posicion[0], int(posicion[1])
    for i in range(len(desplazamientos_x)):
        dx = desplazamientos_x[i]
        dy = desplazamientos_y[i]
        nueva_letra = chr(ord(letra) + dx)
        nuevo_numero = numero + dy
        if 'a' <= nueva_letra <= 'h' and 1 <= nuevo_numero <= TAMANODELTABLERO:
            indice_x = 8 - nuevo_numero
            indice_y = ord(nueva_letra) - ord('a')
            casilla = tablero[indice_x][indice_y]
            if casilla == '' or casilla[-1] != color:
                movimientos.append(f"{nueva_letra}{nuevo_numero}")
    return movimientos


def main():
    # Crea un tablero vacío de 8x8 para el juego de ajedrez
    tablero = [['' for _ in range(TAMANODELTABLERO)] for _ in range(TAMANODELTABLERO)]

    # Solicita al usuario la cantidad de piezas que desea ingresar al tablero
    while True:
        try:
            cantidad_piezas = int(input("¿Cuántas piezas desea ingresar?: "))
            if cantidad_piezas > 0:
                break
            else:
                print("Por favor, ingrese un número mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Loop para ingresar cada pieza en el tablero
    for _ in range(cantidad_piezas):
        pieza, color, posicion = usuario_ingresar_la_pieza()
        letra, numero = posicion[0], int(posicion[1])
        tablero[8 - numero][ord(letra) - ord('a')] = pieza + color

    # Ingreso específico para un caballo, que será usado para mostrar sus posibles movimientos
    pieza, color, posicion = usuario_ingresar_la_pieza(es_caballo=True)
    tablero[8 - int(posicion[1])][ord(posicion[0]) - ord('a')] = pieza + color
    # Imprime el tablero con las piezas colocadas
    print("\nTablero con piezas:")
    tablero_juego(tablero)
    # Calcula y muestra los posibles movimientos del caballo desde su posición
    movimientos_caballo = que_movimientos_del_caballo_hay(posicion, tablero, color[0].upper())
    print("\nPosibles movimientos del caballo:")
    for movimiento in movimientos_caballo:
        letra, numero = movimiento[0], int(movimiento[1])
        pieza_en_movimiento = tablero[8 - numero][ord(letra) - ord('a')]
        if pieza_en_movimiento:
            print(f"{movimiento} con {pieza_en_movimiento}")
        else:
            print(f"{movimiento}, vacía")

if __name__ == "__main__":
    main()
