#!/usr/bin/python3
# Importación de bibliotecas
import numpy as np
import pygame
import sys
import socket
import threading


# Aqui se van a definir las funciones para el manejo de filas y columnas
# Primero se van a definir algunas funciones necesarias para encontrar
# posiciones, revisar la condicion de win etc...
# Todas las reglas van a ser alrededor de una matriz, donde mas
# adelante se va a definir el tablero con pygames
# Se crea primero el board
def Matrix_of_board():
    """
    Crea y devuelve una matriz que representa el tablero.

    Al ser llamada genera una matriz de 6 filas por 7 columnas,
    utilizando la biblioteca NumPy. Cada elemento de la matriz
    se inicializa con el valor cero (0).

    Retorna:
    - board: Una matriz de NumPy de dimensiones 6x7,
    con todos los elementos inicializados en 0.
    """
    board = np.zeros((6, 7))
    return board


# Se crea la siguiente función para que coloque un 1
# o 2 en la matriz simulando una pieza
def number_valid_in_matrix(board, row, col, piece):
    """
    Coloca un 1 o 2 en una posición específica del tablero de juego.

    Esta función se utiliza para modificar el tablero matriz del
    juego.
    Asigna un valor específico en la posición dada de la matriz,
    simulando la colocación de una pieza en el juego.

    Parámetros:
    - board: Matriz que representa el tablero del juego.
    - row: Entero que indica la fila en la matriz donde se colocará la pieza.
    - col: Entero que indica la columna en la matriz donde colocará la pieza.
    - piece: Valor que representa la pieza que se colocará en el tablero.
             1 jugador 1, 2 para el jugador 2.

    La función no retorna ningún valor, pero modifica la matriz 'board' pasada,
    colocando el valor 'piece' en la posición (fila 'row', columna 'col')
    del tablero.
    """
    # Coloca la pieza en la posición especificada en el tablero.
    board[row][col] = piece


# Esta función tiene el objetivo de revisar sí el tablero está lleno, es decir
# si es posible poner todavía una pieza en el tablero retorne True
def Fullboard_matrix(board, col):
    """
    Verifica si hay espacio en una columna específica del tablero disponible
    para colocar una pieza.

    Parámetros:
    - board: Matriz representando el tablero de juego
    - col: Índice de la columna a revisar (entero).

    La función itera por cada fila en la columna dada. Si encuentra
    una celda con valor 0, indica que hay espacio y retorna True. Si todas las
    celdas tienen valor diferente de 0, indica que la columna está llena y
    retorna False.

    Retorna:
    - True: Si al menos una celda en la columna está vacía (valor 0).
    - False: Si todas las celdas en la columna están ocupadas.
    """
    # Si la columna está llena, retorna False.
    for row in range(board.shape[0]):
        if board[row][col] == 0:
            return True
    return False


# Esta revisa cual es la primera fila vacia para pode poner la ficha,
# de abajo hacia arriba
def Empty_row_matrix(board, col):
    """
    Encuentra la primera fila vacía en una columna del tablero,
    empezando por la parte de abajo.

    Esta función busca la fila más baja disponible en una columna para colocar
    una ficha.

    Parámetros:
    - board: Matriz representando el tablero del juego.
    - col: Índice de la columna a revisar.

    La función itera sobre las filas de la columna especificada, comenzando
    desde la fila más baja. Si encuentra una celda vacía (valor 0), retorna
    el índice de esa fila. Si la columna está completamente llena, retorna
    None.

    Retorna:
    - Índice de la primera fila vacía (entero), o None si la columna está
    llena.
    """
    # Retorna el índice de la primera fila vacía en la columna dada,
    # de abajo hacia arriba. Si la columna está llena, retorna None.
    for row in range(board.shape[0] - 1, -1, -1):
        if board[row][col] == 0:
            return row
    return None


# A continuación se van a definir las funciones necesarias para implementar
# cuando se gana se pierde...
# Esta revisa si en una lista hay cuatro seguidos, se usa adelante
# en la revisión de filas y columnas
def four_in_a_row_list(lst):
    """
    Determina si hay cuatro elementos iguales y consecutivos en una lista.

    Esta función verifica si en la lista proporcionada hay una secuencia de
    cuatro elementos iguales y consecutivos que no sean cero. Se utiliza para
    revisar donde hay cuatro fichas iguales seguidas.

    Parámetros:
    - lst: Lista de valores numéricos que se revisará.

    La función itera sobre los elementos de la lista, revisando grupos de
    cuatro elementos consecutivos. Si encuentra un grupo donde todos los
    elementos son iguales y diferentes de cero, retorna True. En caso
    contrario, retorna False.

    Retorna:
    - True: Si hay cuatro elementos iguales y no cero consecutivos en la lista.
    - False: Si no se encuentra tal secuencia en la lista.
    """
    for i in range(len(lst) - 3):
        if lst[i] == lst[i+1] == lst[i+2] == lst[i+3] != 0:
            return True
    return False


# Aqui se van a revisar las filas horizontalmente con la condición de victoria
def check_horizontal(board):
    """
    Revisa si hay una secuencia ganadora horizontal en el tablero de juego.

    Esta función recorre todas las filas del tablero de juego y utiliza
    'four_in_a_row_list' para verificar si hay una secuencia de cuatro fichas
    iguales y consecutivas en alguna fila.
    Parámetros:
    - board: Matriz que representa el tablero del juego.

    Si 'four_in_a_row_list' retorna True esta función también retorna True.
    Si no hay ninguna secuencia ganadora en todas las filas, retorna False.

    Retorna:
    - True: Si hay cuatro elementos horizontal iguales.
    - False: Si no hay cuatro elementos seguidos iguales.
    """
    for row in range(board.shape[0]):
        if four_in_a_row_list(list(board[row, :])):
            return True
    return False


# Aqui se van a revisar verticalmente con la condicion de victoria
def check_vertical(board):
    """
    Revisa si hay una secuencia ganadora vertical en el tablero de juego.

    Esta función recorre todas las columnas del tablero de juego y utiliza la
    función 'four_in_a_row_list' para verificar si hay una secuencia de cuatro
    fichas iguales y consecutivas en alguna columna.

    Parámetros:
    - board: Matriz que representa el tablero del juego.

    Si 'four_in_a_row_list' retorna True esta función también retorna True.
    Si no hay ninguna secuencia ganadora en todas las filas, retorna False.

    Retorna:
    - True: Si hay cuatro elementos horizontal iguales.
    - False: Si no hay cuatro elementos seguidos iguales.
    """
    for col in range(board.shape[1]):
        if four_in_a_row_list(list(board[:, col])):
            return True
    return False


# Aquí se van a revisar las filas, columnas y diagonales
# con la condición de victoria
# Se revisar las diagonales en de abajo hacia arriba y viceversa
# en dos ciclos for diferentes para simplificar la lógica
def check_diagonal(board):
    """
    Revisa si hay una secuencia ganadora en las diagonales del tablero.

    Esta función revisa todas las diagonales del tablero para ver si hay
    una secuencia de cuatro fichas iguales y seguidas. Se revisan tanto las
    diagonales con de manera positiva (de abajo hacia arriba) como
    de manera negativa (de arriba hacia abajo).

    Parámetros:
    - board: Matriz que representa el tablero del juego.

    Si 'four_in_a_row_list' retorna True esta función también retorna True.
    Si no hay ninguna secuencia ganadora en todas las filas, retorna False.

    Retorna:
    - True: Si hay cuatro elementos horizontal iguales.
    - False: Si no hay cuatro elementos seguidos iguales.
    """
    # Revisar diagonales con pendiente positiva
    for col in range(board.shape[1] - 3):
        for row in range(board.shape[0] - 3):
            if board[row][col] == board[row + 1][col + 1] == \
               board[row + 2][col + 2] == board[row + 3][col + 3] != 0:
                return True

    # Revisar diagonales con pendiente negativa
    for col in range(board.shape[1] - 3):
        for row in range(3, board.shape[0]):
            if board[row][col] == board[row - 1][col + 1] == \
               board[row - 2][col + 2] == board[row - 3][col + 3] != 0:
                return True

    return False


# Esta simplemente revisa los flase o true de las funciones
# de revision de victoria
def check_win(board):
    """
    Determina si hay un ganador en el tablero de juego.

    Esta función verifica las condiciones de victoria en el tablero de juego,
    comprobando si hay una secuencia ganadora horizontal, vertical o diagonal.

    Parámetros:
    - board: Matriz que representa el tablero del juego.

    Si 'check_horizontal', 'check_vertical',
    o 'check_diagonal' retorna True, indica que hay un ganador y la
    función 'check_win' también retorna True. Si no se encuentra
    ganadora, retorna False.

    Retorna:
    - True: Si hay un ganador.
    - False: Si no se encuentra un ganador.
    """
    return check_horizontal(board) or check_vertical(
        board) or check_diagonal(board)


# Esta revisa si hay empate
def check_draw(board):
    """
    Determina si el juego ha terminado en empate.

    Esta función revisa si todas las celdas del tablero de juego están
    ocupadas, lo que indica un empate, mientras no haya un ganador ya.

    Parámetros:
    - board: Matriz que representa el tablero del juego.

    La función recorre todas las celdas. Si encuentra una celda vacía
    (valor 0), retorna False, indicando que el juego aún no ha terminado. Si
    todas las celdas están ocupadas, utiliza la función 'check_win'
    para ver si hay un ganador. Si no, entonces retorna True, indicando un
    empate.

    Retorna:
    - True: Si el tablero está lleno y no hay un ganador.
    - False: Si todavía hay celdas vacías o hay un ganador.
    """
    for col in range(board.shape[1]):
        for row in range(board.shape[0]):
            if board[row][col] == 0:
                return False  # Todavía hay un espacio vacío, no es empate
    return not check_win(board)  # Es empate solo si nadie ha ganado


# Se usa para el debug, eliminar cuando se vea
board = Matrix_of_board()
print(board)

# A partir de aquí se va a tomar en cuenta la biblioteca de pygames para
# poder lograr el tablero adecuadamente
# Para dibujo
pygame.init()
# Para sonido
pygame.mixer.init()
# Para que se empiece en el menú
estado = 'menu'
# Variable para inicilizar al jugador
# en local, si no se utiliza cuando el juego es en
# linea eliminar
jugador = 1

# Algunos sonidos para implementar el juego
# Sonido de las piezas
sound_drop_piece_charge = pygame.mixer.Sound('Drop_piece.wav')
sound_drop_piece_charge.set_volume(0.5)

# Sonido de el start
sound_start_game = pygame.mixer.Sound('Start_game.wav')
sound_start_game.set_volume(0.5)

# Sonido de cuando gana un jugador
sound_end_game = pygame.mixer.Sound('End_game.wav')
sound_end_game.set_volume(0.5)

# Sonido de el exit
sound_exit_game = pygame.mixer.Sound('Quit_memu.mp3')
sound_exit_game.set_volume(0.5)

# Sonido de ambiente del menu
sound_ambien_menu = pygame.mixer.Sound('Ambien_menu.wav')
sound_ambien_menu.set_volume(0.5)

# Aqui se va a cargar una fuente para el texto
# para que el estilo sea mas de tipo juego
font_path = 'Pixel_Bug.otf'
font_size = 40
game_font = pygame.font.Font(font_path, font_size)

# Aquí pasamos a los parámetros de screen y sobre
# el dibujo del tablero y color del fondo
# Constantes para el tamaño de la pantalla
# Tamaño de la pantalla
SQUARESIZE = 110
# Como quiero un rectángulo entonces añado este parámetro para
# luego añadirlo a la pantalla
additional_width = 600
width = 7 * SQUARESIZE + additional_width
height = (6 + 1) * SQUARESIZE
# Radio de los círculos del tablero y fichas, son iguales
RADIUS = int(SQUARESIZE / 2 - 7)
size = (width, height)

# Como se añadió espacio a los lados para que la pantalla fuera un
# un rectángulo y debemos dibujar todo en el centro, se calculó
# este inicio para que sea la mitad del rectángulo
board_start_x = additional_width // 2

# Colores utilizados en el dibujo con pygames
BLACK = (0, 0, 0)
BOARD_COLOR = (0, 30, 0)
RED = (255, 0, 0)
RED_low = (200, 0, 0)
YELLOW = (255, 255, 0)
YELLOW_low = (200, 200, 0)
WHITE = (255, 255, 255)
WHITE_low = (170, 170, 170)
Line = (230, 230, 230)

# Configurar pantalla
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Four in a Row")

# Establecer conexión con el servidor
# Esta configuracón solo permite conectarse
# a clientes de la sub red local.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.0.2.15', 5555)
client_socket.connect(server_address)

# Recibir el ID del jugador y el turno inicial
data = client_socket.recv(1024).decode()
player_id, current_turn = map(int, data.split(','))

# Mostrar información de depuración, eliminar si se desea
print(f"Conectado al servidor. ID del Jugador: {player_id},"
      f"Turno Inicial: {current_turn}")


# Funciones para dibujar
# Funcion para dibujar el tablero, se intento un atablero con esquinas
# redondeadas para una mejor estetica en el juego
def draw_rounded_rect(surface, color, rect, corner_radius):
    """
    Dibuja un rectángulo con esquinas redondeadas en un la pantalla.

    Esta tiene el objetivo de mejorar la visualización y estetica
    del juego, creando un tablero con bordes redondeados para mejorar
    la experiencia del jugador.
    Se utiliza la biblioteca Pygame para el dibujo.

    Parámetros:
    - surface: Pantalla de Pygame donde se dibujará el rectángulo.
    - color: Color del rectángulo.
    - rect: Tupla o lista que define la posición y tamaño del rectángulo
      (x, y, ancho, alto).
    - corner_radius: Radio de las esquinas redondeadas.

    La función descompone el rectángulo en sus partes (x, y, ancho, alto)
    y dibuja las esquinas redondeadas y los lados rectos para formar
    un rectángulo completo con esquinas redondeadas.

    No retorna nada.
    """
    # Se descomprime el rectángulo y dibuja las partes redondeadas
    rect_x, rect_y, rect_w, rect_h = rect
    circle_diameter = 2 * corner_radius
    # Se dibuja un cuadrado de altura + radio y ancho - radio
    pygame.draw.rect(surface, color, (rect_x + corner_radius,
                                      rect_y, rect_w - circle_diameter,
                                      rect_h))
    # Lo mismo del anterior pero al contrario
    pygame.draw.rect(surface, color, (rect_x, rect_y + corner_radius,
                                      rect_w, rect_h - circle_diameter))
    # Cada una de las siguientes cuatro lineas dibuja un circulo en cada
    # esquina
    pygame.draw.circle(surface, color, (rect_x + corner_radius,
                                        rect_y + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect_x + rect_w - corner_radius,
                                        rect_y + corner_radius), corner_radius)
    pygame.draw.circle(surface, color,
                       (rect_x + corner_radius,
                        rect_y + rect_h - corner_radius), corner_radius)
    pygame.draw.circle(surface, color,
                       (rect_x + rect_w - corner_radius,
                        rect_y + rect_h - corner_radius), corner_radius)


# Esta funcion busca dibujar unas lineas
# para que ayude al usuario saber los limites
# en los cuales hacer click para colocar una ficha
def draw_lines(surface, columns, square_size, start_y, end_y):
    """
    Dibuja líneas verticales para indicar los límites de
    las columnas en el tablero de juego.

    Esta función es para darle al usuario una referencia visual
    de los límites en los que puede hacer clic para colocar una ficha en el
    juego. Se utiliza la biblioteca Pygame para el dibujo.

    Parámetros:
    - surface: Pantalla de Pygame donde se dibujarán las líneas.
    - columns: Número de columnas del tablero.
    - square_size: Tamaño de cada cuadrado del tablero.
    - start_y: Coordenada Y donde comienzan las líneas.
    - end_y: Coordenada Y donde terminan las líneas.

    Las líneas se dibujan con un grosor definido por 'line_width', y se
    colocan en el centro entre dos columnas del tablero.

    No retorna nada.
    """
    line_width = 8  # El grosor de las líneas
    for col in range(1, columns):
        # La línea se dibujará en la mitad entre dos columnas.
        # Se ayuda de la posición de board_start_x para tener una
        # referencia
        line_x = 3 + board_start_x + col * square_size - (line_width // 2)
        pygame.draw.line(surface, Line, (line_x, start_y),
                         (line_x, end_y), line_width)


# Esta funcion es utilizada para que se impriman
# las fichas cuandos se cambie de un 0 a 1 o 2 en la matriz
def piece_board(board):
    """
    Dibuja fichas en el tablero según el estado de la matriz del juego.

    Esta función recorre la matriz del tablero de juego y dibuja fichas en las
    posiciones correspondientes. Las fichas son representadas por círculos en
    por Pygame. Se dibujan fichas de dos colores diferentes,
    dependiendo del valor en la matriz del tablero (1 o 2), para identificar
    a cada jugador.

    Parámetros:
    - board: Matriz que representa el tablero del juego.

    Si el valor de la celda es 1, dibuja una ficha de color
    'RED', y si es 2, una ficha de color 'YELLOW'. También se dibuja un círculo
    interior de un tono más claro para dar un efecto visual.

    No retorna nada.
    """
    for c in range(board.shape[1]):
        for r in range(board.shape[0]):
            pos_x = board_start_x + int(c * SQUARESIZE + SQUARESIZE / 2)
            pos_y = (r * SQUARESIZE) + 3 * SQUARESIZE / 2
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (pos_x, pos_y), RADIUS)
                pygame.draw.circle(screen, RED_low, (pos_x, pos_y), RADIUS-10)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (pos_x, pos_y), RADIUS)
                pygame.draw.circle(screen, YELLOW_low,
                                   (pos_x, pos_y), RADIUS-10)


# Esta funcion toma todas las funciones anteriores y revisa el
# board para imprimir cuando se modifique la matriz, todo
# el juego usa la matriz como una referencia para
# imprimir fichas, las cantidades de columnas, etc...
def draw_board(board):
    """
    Dibuja el tablero de juego y actualiza su estado en la pantalla.

    Esta función es la responsable de actualizar la interfaz gráfica del juego.
    Rellena el fondo, dibuja un rectángulo con bordes redondeados,
    añade líneas divisorias para las columnas y muestra el turno del
    jugador actual. Se utilizan las funciones anteriores.

    Parámetros:
    - board: Matriz que representa el tablero del juego.

    Primero, se rellena el fondo con el color del tablero. Luego, se dibujan
    los elementos del tablero como el rectángulo principal y las líneas
    divisorias.
    Se actualiza la pantalla con 'pygame.display.update'.

    No retorna nada.
    """
    screen.fill(BOARD_COLOR)  # Rellenar el fondo
    draw_rounded_rect(screen, WHITE, (board_start_x,
                                      SQUARESIZE, 7 * SQUARESIZE,
                                      height - SQUARESIZE), 60)
    draw_lines(screen, 7, SQUARESIZE, SQUARESIZE, height)
    show_turn(screen, jugador)

    for c in range(board.shape[1]):
        for r in range(board.shape[0]):
            pos_x = board_start_x + int(c * SQUARESIZE + SQUARESIZE / 2)
            pos_y = height - int(r * SQUARESIZE + SQUARESIZE / 2)
            pygame.draw.circle(screen, BLACK, (pos_x, pos_y), RADIUS)
            pygame.draw.circle(screen, WHITE_low, (pos_x, pos_y), RADIUS - 7)

    # Dibuja las fichas después de haber dibujado el tablero.
    piece_board(board)
    pygame.display.update()


# Esta funcion tiene el objetivo de determinar cual es el turno del jugador
# para ayudar al jugador a identificar si es su turno o no
def show_turn(screen, player):
    """
    Muestra en la pantalla cuál jugador tiene el turno actual.

    Esta función es utilizada para que los jugadores sepan a quién le toca
    el turno actual en el juego. Muestra un mensaje en la pantalla que indica
    si es el turno del jugador 1 o del jugador 2.

    Parámetros:
    - screen: Superficie de Pygame donde se mostrará el turno.
    - player: Identificador del jugador actual.

    Primero, muestra el identificador del jugador actual. Luego, dependiendo
    del estado de la variable 'current_turn', muestra un mensaje indicando si
    es el turno del jugador 1 (color rojo) o del jugador 2 (color amarillo).

    No retorna nada.
    """
    labelid = game_font.render(f"Jugador {player_id}", 1, WHITE)
    screen.blit(labelid, (100, 60))
    # Utilizado para el tipo de letra y el tamño de la letra
    if current_turn == 1:
        # Lo que se imprime si es el jugador uno
        label = game_font.render("Turno del Jugador 1", 1, RED_low)
    else:
        # Lo que se imprime si es el jugador 2
        label = game_font.render("Turno del Jugador 2", 1, YELLOW_low)
    screen.blit(label, (100, 10))


# Funcion para imprimir si gano o empato el jugador al final de
# la partida
def game_over_message(winner):
    """
    Muestra un mensaje de victoria o empate al finalizar la partida.

    Esta función se activa al final de un juego para que se sepa
    sobre el resultado de la partida: si ganó el jugador 1, el jugador 2, o si
    fue un empate. Muestra un mensaje en pantalla con el resultado y una
    instrucción para volver al menú principal.

    Parámetros:
    - winner: El número del jugador ganador o 0 en caso de empate.

    La función rellena la pantalla con un fondo negro y muestra el mensaje
    correspondiente al resultado de la partida. También espera a que el usuario
    haga clic para continuar, lo que permite leer el mensaje con calma.

    No retorna nada.
    """
    # Mostrar el mensaje de victoria o empate
    global estado
    screen.fill(BLACK)  # Fondo negro para el mensaje
    font = game_font
    if winner == 1:
        text = "El jugador 1 gana!"
        color = RED
    elif winner == 2:
        text = "El jugador 2 gana!"
        color = YELLOW
    else:
        text = "Empate!"
        color = WHITE

    label = font.render(text, 1, color)
    screen.blit(label, (width // 2 - label.get_width() // 2,
                        height // 2 - label.get_height() // 2))

    subtext = "Haz clic para volver al menú"
    sublabel = font.render(subtext, 1, WHITE)
    screen.blit(sublabel, (width // 2 - sublabel.get_width() // 2,
                           height // 2 + label.get_height()))

    pygame.display.flip()

    # Esperar al clic del usuario para continuar
    waiting_for_click = True
    while waiting_for_click:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting_for_click = False


# Menu del juego, esta función es utilizada para crear una pantalla de menu
# al inicio y al final del juego
def show_menu():
    """
    Muestra el menú principal del juego.

    Esta función crea y muestra el menú principal del juego, con opciones para
    iniciar una nueva partida o salir del juego. Carga y muestra botones de
    'Start' y 'Exit', y maneja las interacciones del usuario con estos
    botones.

    No toma parámetros ni retorna nada.

    Utiliza la biblioteca Pygame para la creación de la interfaz gráfica.
    Al hacer clic en el botón 'Start', se inicia una nueva partida.
    Al hacer clic en 'Exit', se cierra el juego. La función también
    cumple la carga y escalado
    de las imágenes de los botones, así como su posicionamiento en la pantalla.
    """
    global estado
    global board
    menu_color = (230, 230, 230)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Menú del Juego")
    screen.fill(menu_color)

    # Carga de imágenes
    play_button_image = pygame.image.load('Start.png').convert_alpha()
    exit_button_image = pygame.image.load('Exit.png').convert_alpha()

    # Escala las imágenes a el tamaño deseado
    play_button = pygame.transform.scale(play_button_image, (200, 100))
    exit_button = pygame.transform.scale(exit_button_image, (200, 100))

    # Posiciones de los botones
    play_button_pos = play_button.get_rect(center=(board_start_x + 400, 250))
    exit_button_pos = exit_button.get_rect(center=(board_start_x + 400, 400))

    # Bucle principal
    running = True
    while running:
        # Eventos
        estado = 'terminado'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detecta el clic del mouse con el botón
                if play_button_pos.collidepoint(event.pos):
                    sound_start_game.play()
                    print("Iniciar juego!")
                    # Para reiniciar siempre que se comience un
                    # juego nuevo, se vacia la matriz
                    board = Matrix_of_board()
                    estado = 'progreso'
                    running = False
                elif exit_button_pos.collidepoint(event.pos):
                    sound_exit_game.play()
                    pygame.time.delay(800)
                    running = False

        # Fondo
        screen.fill(menu_color)

        # Dibuja los botones
        screen.blit(play_button, play_button_pos)
        screen.blit(exit_button, exit_button_pos)

        # Actualizar la pantalla
        pygame.display.flip()


def listen_to_server():
    """
    Escucha la información del servidor y actualiza el tablero y el turno.

    Esta función se ejecuta en un hilo separado y está en constante escucha
    de mensajes del servidor. Al recibir un mensaje, actualiza el tablero y
    el turno actual en el juego con la información
    recibida del servidor.

    No toma parámetros ni retorna nada.

    En cada iteración, la función espera recibir un mensaje del servidor.
    Este mensaje contiene información sobre la columna jugada y el turno
    actual. Utiliza esta información para actualizar la matriz del tablero y
    cambiar el turno.
    """
    global current_turn, board
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                received_column, received_turn = map(int, message.split(','))
                # Imprimir para depuración
                print(f"Mensaje recibido del servidor:"
                      f"Columna = {received_column}, Turno = {received_turn}")

                # Actualizar el tablero y el turno
                # basándose en la información recibida
                row = Empty_row_matrix(board, received_column)
                if row is not None:
                    number_valid_in_matrix(board, row,
                                           received_column, current_turn)
                    print(board)
                    current_turn = received_turn
                    print(f"Tablero actualizado. Turno actual: {current_turn}")
        except Exception as e:
            print(f"Error al recibir datos del servidor: {e}")
            break


# Iniciar el hilo de escucha, se utiliza para que
# no se tenga que esperar a que el server mande
# la información y pueda causar problemas, es
# basicamente para que sea posible la multitarea,
# sin esta linea no se actualiza el tablero puesto
# que no realiza la multitarea
threading.Thread(target=listen_to_server, daemon=True).start()


# Esta función es para configurar los eventos en pygames, principalmente que
# que los se detecte el cursor y cmabie entre jugadores, etc
def main_game():
    """
    Maneja la lógica principal y los eventos del juego en curso.

    Esta función controla el juego, gestionando eventos de Pygame,
    clics de mouse y cierre del juego. Permite
    enviar movimientos al servidor y actualizando el tablero en función
    de los turnos y el estado del juego.

    No toma parámetros ni retorna nada.

    Dentro del bucle principal, la función maneja eventos como clics del mouse
    para colocar fichas, verifica las condiciones de victoria o empate, y
    actualiza la interfaz gráfica. Si un jugador gana o si el juego termina
    en empate, llama a las funciones correspondientes.
    """
    global estado, jugador, board
    while estado == 'progreso':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_drop_piece_charge.play()
                print(event)

                # Solo el jugador cuyo turno sea actual puede jugar
                if player_id == current_turn:
                    x_pos = event.pos[0] - board_start_x
                    if x_pos >= 0 and x_pos <= width - additional_width:
                        col = int(x_pos / SQUARESIZE)

                        if Fullboard_matrix(board, col):
                            # Envía el número de columna al servidor
                            client_socket.sendall(str(col).encode())

            if check_win(board):
                print(f'El jugador {current_turn} gana')
                sound_end_game.play()
                if current_turn == 2:
                    game_over_message(current_turn-1)
                else:
                    game_over_message(current_turn+1)
                estado = 'menu'
                break
                # Cambia el turno del jugador localmente para
                # evitar más movimientos hasta recibir actualización
                # revisar si es necesaria sino eliminar porque la variable
                # jugador se utilizaba localmente
                jugador = 3 - jugador

            if check_draw(board):
                print('Empate')
                sound_end_game.play()
                game_over_message('Empate')
                estado = 'menu'
                break

        draw_board(board)
        pygame.display.flip()


# Este va a ser el bucle principal del juego, donde va a empezar el juego,
# ir al juego, volver al menu, terminar el programa, etc
while True:
    if estado == 'menu':
        sound_ambien_menu.play(-1)
        show_menu()
    elif estado == 'progreso':
        sound_ambien_menu.stop()
        main_game()
    elif estado == 'game_over':
        game_over_message(jugador)
    elif estado == 'terminado':
        break

pygame.quit()
sys.exit()
