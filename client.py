import socket
import pickle
# import netifaces as ni

# def client():
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!q"

SERVER = 'localhost'
PORT = 5678
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)

    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    recv_msg = client.recv(100000000).decode(FORMAT)

    return recv_msg

print(send("Hello World!"))
