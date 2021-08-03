import socket
from threading import Thread
import datetime

MAX_CONNECTIONS =  5
BUFFER_SIZE = 1024 # razoável me thinks

client_sockets = []

# Config
valid = False
while not valid:
    try:
        HOST, PORT = input("Host IP: ").split(':')
        PORT = int(PORT)
        
        host_socket = socket.socket()
        host_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        host_socket.bind((HOST,PORT))

        valid = True
    except Exception as e:
        print(e)

print(f"Ouvindo como {HOST}:{PORT}.")

# Ativar o socket para MAX_CONNECTIONS ligações vindouras
host_socket.listen(MAX_CONNECTIONS)

# A partir daqui, podem ser aceites conexões

# Aqui a função para lidar com uma conexão
def handle(client_socket, client_address):
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

# Com a função definida, criar tarefas (threads) para cada uma das conexões recebidas

def getCommands():
    com = ""
    while com != "/q":
        com = input(" > ").split(' ')
        if (com[0] == "/q"):
            for cs in client_sockets:
                try:
                    cs.send( "Servidor encerrado".encode() )
                    cs.close()
                except Exception:
                        pass
            return
        elif(com [0] == "/b"):
            if len(com) < 2:
                print("Insira uma mensagem após /b!")
            else:
                msg = ""
                for word in com[1:]:
                    msg = msg + word
                for cs in client_sockets:
                    try:
                        cs.send( (f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] SERVIDOR > {msg}").encode() )
                    except Exception:
                        pass

def listen():
    while True:
        client_socket, client_address = host_socket.accept()

        client_thread = Thread ( target=handle, args=(client_socket, client_address,) )

        client_thread.daemon = True

        client_thread.start()

listener = Thread ( target=listen )
listener.daemon = True
listener.start()

getCommands()