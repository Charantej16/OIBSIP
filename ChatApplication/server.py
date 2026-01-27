import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}
print("Server started...")


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            remove_client(client)


def remove_client(client):
    if client in clients:
        name = clients[client]
        del clients[client]
        broadcast(f"🔴 {name} left the chat\n".encode())


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            remove_client(client)
            break


def receive():
    while True:
        client, address = server.accept()
        name = client.recv(1024).decode()
        clients[client] = name

        broadcast(f"🟢 {name} joined the chat\n".encode())
        print(f"{name} connected")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


receive()


