import socket
import threading

Port = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',Port))
server.listen()

clients,nicknames = [],[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f'{nickname[clients.index(client)]} says {message}')
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


def recieve():
    while True:
        client,address = server.accept()
        print(f'Connected with address {str(address)}')

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send('Connected to the server'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))

print('Server running...')
recieve()

