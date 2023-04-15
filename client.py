import socket
import threading

nickname=input('enter a nickname: ')

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',57777))

def receive():
    while True:
        try:
            message=client.recv(1024).decode()

            if message=="NICK":
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print("an error occurred")
            client.close()
            break

def write():
    while True:
        message="{} :{}".format(nickname,input(''))
        client.send(message.encode())

receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()

            
        
