import socket
import datetime
from threading import Thread

BUFFER_SIZE = 1024 # razoável me thinks

valid = False
while not valid:
    try:
        SERVER, PORT = input("IP: ").split(':')
        PORT = int(PORT)
        
        client_socket = socket.socket()
        client_socket.connect((SERVER,PORT))

        valid = True
    except Exception as e:
        print(e)
        
NICKNAME = input("Nickname: ").lower()

def getSignature():
    return f"[{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] {NICKNAME}"

client_socket.send( (f"{getSignature()} conectou-se.").encode() )

print(f"Conetado a {SERVER}:{PORT}.")

def getBroadcast():
    while True:
        try:
            received = client_socket.recv(BUFFER_SIZE).decode()
        except Exception:
            return
        else:
            print(received)

def sendMessage():
    while True:
        message = input(" > ")
        if len(message) > 0:
            if message[0] == "/":
                client_socket.send( (f"{getSignature()} desconectou-se.").encode() )
                client_socket.send( "<DISCONNECT>".encode() )
                client_socket.close()
            else:
                client_socket.send( (f"{getSignature()} > {message}").encode() )

# Execute

listener = Thread ( target=getBroadcast )

listener.daemon = True

listener.start()

sendMessage()