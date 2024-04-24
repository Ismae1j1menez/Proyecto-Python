#!/usr/bin/python3
import socket
import threading


def client_thread(conn, players, player_id, current_turn):
    """
    Maneja la comunicación con el cliente.

    Esta función se ejecuta en un hilo de escucha para cada cliente que se
    conecta. Se encarga de recibir el número
    de columna seleccionado y reenviar estos movimientos a todos los clientes
    para mantener el juego sincronizado.

    Parámetros:
    - conn: Socket de conexión del cliente.
    - players: Lista de todos los sockets de jugadores conectados.
    - player_id: Identificador del jugador asociado a este hilo.
    - current_turn: Diccionario compartido que guarda el turno actual.

    La función permanece en un bucle que escucha mensajes del cliente. Al dar
    un mensaje, cambia el turno y reenvía el mensaje a todos los clientes. Si
    ocurre un error o el cliente se desconecta, el bucle se rompe.
    """
    while True:
        try:
            # Recibir mensaje del cliente (posición de la columna)
            column = conn.recv(1024).decode()

            # Este es el caracter vacio para detectar la conexión
            if column == "":
                print(f"Cliente {player_id} desconectado.")
                break

            print(f"Recibido del cliente {player_id}: {column}")

            # Simplemente cambia el turno del jugador y lo envia al cliente
            # principalmente para que sea justo y el server sincronice
            # los ambos clientes
            current_turn["turn"] = 1 if current_turn["turn"] == 2 else 2
            message = f"{column},{current_turn['turn']}"
            for player in players:
                print(f"Enviando a cliente: {message}")
                player.sendall(message.encode())

        except Exception as e:
            print(f"Error o desconexión del cliente {player_id}: {e}")
            break


# Se llama al contructor de la clase para instanciar una IPv4 ya
# que es para la red local y con un socket orientado a la conexion,
# ya que son pocos datos que estos lleguen intactos.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Importante como es para una red sublocal se debe poner la IP
# de la red interna para que el cliente
# se pueda conectar
server.bind(('10.0.2.15', 5555))
# Que escuche a solo dos clientes
server.listen(2)

players = []
player_id = 1
current_turn = {"turn": 1}

print("Servidor iniciado. Esperando jugadores...")

# Mientras que sea menor a dos clientes se puede conectar al server, es
# decir lo limita a solo dos clientes
while len(players) < 2:
    # Dentro del bucle while donde se aceptan las conexiones de los clientes
    conn, addr = server.accept()
    print(f"Jugador {player_id} ({addr}) conectado.")

    # Enviar el número de jugador y el turno inicial al cliente
    mensaje_inicial = f"{player_id},{current_turn['turn']}"
    conn.sendall(mensaje_inicial.encode())

    # Agregar el cliente a la lista y empezar
    players.append(conn)
    threading.Thread(target=client_thread, args=(
        conn, players, player_id, current_turn)).start()
    player_id += 1


print("Todos los jugadores conectados. El juego puede comenzar.")
