# Proyecto-Python
Este es el repositorio donde se trabajar el proyecto de Python, curso: IE-0117 Programación Bajo Plataformas Abiertas

## Proyecto de Juego en Red: Cuatro en Línea
Este proyecto implementa una versión del juego clásico "Cuatro en Línea" jugable sobre una red local utilizando Python, la librería Pygame para la interfaz gráfica y sockets para la comunicación en red.

## Características Principales

- **Interfaz Gráfica:** Utiliza Pygame para la representación gráfica del tablero de juego, dibujo de fichas y manejo de eventos de usuario.
- **Red de Comunicaciones:** Implementa la comunicación entre múltiples clientes y un servidor usando sockets, permitiendo partidas en tiempo real.
- **Sonido y Estética Visual:** Incluye efectos de sonido para las acciones del juego y utiliza un diseño visual atractivo con esquinas redondeadas y colores llamativos.

## Estructura del Código

El código está dividido en dos partes principales:

1. **Servidor (`Server.py`):**
    - Maneja las conexiones entrantes de los jugadores.
    - Gestiona el flujo del juego y sincroniza el estado del tablero entre todos los clientes.
    - Cambia el turno entre jugadores y retransmite las jugadas a todos los clientes conectados.

2. **Cliente (`Cliente_P4inrow.py`):**
    - Establece conexión con el servidor y maneja la lógica de juego local.
    - Utiliza Pygame para renderizar el tablero de juego, recibir entradas de usuario y mostrar el estado actual del juego.
    - Escucha actualizaciones del servidor para mantener sincronizado el estado del juego.

## Funcionamiento

- Al iniciar, el servidor se pone en espera de conexiones de dos jugadores.
- Cada cliente muestra un menú principal donde pueden iniciar un nuevo juego o salir.
- Una vez ambos jugadores están conectados, pueden interactuar con el juego colocando fichas en el tablero.
- El juego verifica condiciones de victoria como secuencias horizontales, verticales y diagonales de cuatro fichas.
- Se proporcionan mensajes de victoria o empate y la opción de volver al menú principal al finalizar la partida.

## Tecnologías Utilizadas

- **Python:** Para la lógica del servidor y del cliente.
- **Pygame:** Para la interfaz gráfica y manejo de eventos.
- **NumPy:** Para manejar el estado del tablero como una matriz.
- **Sockets:** Para la comunicación en red entre el servidor y los clientes.

Este juego representa una excelente integración de diversas tecnologías en Python, mostrando cómo se pueden utilizar para crear aplicaciones interactivas y en red.

