import socket
import threading

HOST ="127.0.0.1"
PORT =57777

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            nicknames.remove(nickname)
            break

def receive():
    while True:

        client,address = server.accept()
        print("connected with {}".format(str(address)))

        client.send('NICK'.encode())
        nickname=client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print("nickname is {}".format(nickname))
        broadcast("{} has joined the chat".format(nickname).encode())
        client.send('connected to server'.encode())

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()

receive()

