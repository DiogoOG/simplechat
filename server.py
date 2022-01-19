import socket
from threading import Thread
import datetime
import sys

MAX_CONNECTIONS =  10
BUFFER_SIZE = 1024

client_sockets = []
host_socket = socket.socket()

logfilename = f"logs/LOG_{datetime.datetime.now().strftime('%d%m%Y_%H%M%S')}.txt"

def log(line):
    logfile = open(logfilename,"a")
    print(line)
    logfile.write(line + "\n")
    logfile.close()

def connect():

    if len(sys.argv) < 2:
        raise Exception("Poucos argumentos (usar 'server.py IP:PORT').")

    IP, PORT = sys.argv[1].split(':')

    PORT = int(PORT)

    host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    host_socket.bind((IP,PORT))

    log(f"Ouvindo como {IP}:{PORT}.")

    host_socket.listen(MAX_CONNECTIONS)
    
def handle(client_socket,client_address):
    client_sockets.append(client_socket)
    while True:
        try:
            received = client_socket.recv(BUFFER_SIZE).decode()
        except Exception:
            #log(Exception)
            return
        else:
            if "<DISCONNECT>" in received:
                client_socket.close()
            else:
                log(received)
                for cs in client_sockets:
                    try:
                        cs.send( received.encode() )
                    except Exception:
                        #log(Exception)
                        pass

def listener():
    while True:
        client_socket, client_address = host_socket.accept()

        client_thread = Thread ( target=handle, args=(client_socket,client_address,) )

        client_thread.daemon = True

        client_thread.start()

connect()

listener_thread = Thread ( target=listener )

listener_thread.daemon = True

listener_thread.start()

while True:
    pass
