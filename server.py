import socket
from threading import Thread
import sys

MAX_CONNECTIONS =  10
BUFFER_SIZE = 1024

client_sockets = []
host_socket = socket.socket()

def connect():

    if len(sys.argv) < 2:
        raise Exception("Poucos argumentos (usar 'server.py IP:PORT').")

    IP, PORT = sys.argv[1].split(':')

    PORT = int(PORT)

    host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host_socket.bind((IP,PORT))

    print(f"Ouvindo como {IP}:{PORT}.")

    host_socket.listen(MAX_CONNECTIONS)
    
def handle(client_socket,client_address):
    client_sockets.append(client_socket)
    while True:
        try:
            received = client_socket.recv(BUFFER_SIZE).decode()
        except Exception:
            return
        else:
            if "<DISCONNECT>" in received:
                client_socket.close()
            else:
                print(received)
                for cs in client_sockets:
                    try:
                        cs.send( received.encode() )
                    except Exception:
                        pass

def listener():
    while True:
        client_socket, client_address = host_socket.accept()

        client_thread = Thread ( target=handle, args=(client_socket,client_address,) )

        client_thread.daemon = True

        client_thread.start()

def start_listening(listener_thread):
    listener = Thread ( target = listener_thread )
    listener.daemon = True
    listener.start()

connect()
start_listening(listener)

while True:
    pass
