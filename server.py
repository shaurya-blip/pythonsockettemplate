
import socket
import threading

SERVER = 'localhost'

clients = []
HEADER = 64
PORT = 5678
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!q"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr[0]}:{addr[1]} connected")

    connected = True

    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            # print(msg_length)
            msg_length = int(msg_length)
            msg = conn.recv(int(100000000)).decode(FORMAT)

            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr[0]}:{addr[1]}] has disconnected")
                # conn.send("You have been disconnected".encode(FORMAT))
            # print(f"[{addr[1]}] {msg}")

            conn.send(f"200 - {msg}".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        clients.append((conn, addr))
        # print(clients)
        # print(f"[NEW CONNECTION] Client with ip {addr[0]}:{addr[1]} has connected to your server.")

        if threading.activeCount() - 1 > 3:
            print("[ERROR] More than 2 clients are not allowed.")

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


def startserver():
    print(f"[STARTING] SERVER is starting on {str(SERVER)}:{str(PORT)}")
    print(f"[RUNNING] Server is succesfully running....")
    start()


print("______________________________________________________")
startserver()
