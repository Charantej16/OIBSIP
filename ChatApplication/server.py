import socket
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6000

clients = []

def send_to_all(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def client_handler(client_socket, address):
    print(f"User connected from {address}")

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            send_to_all(data, client_socket)
        except:
            break

    print(f"User disconnected from {address}")
    clients.remove(client_socket)
    client_socket.close()

def start_chat_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen()

    print(f"Chat server running on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)

        thread = threading.Thread(
            target=client_handler,
            args=(client_socket, addr)
        )
        thread.start()

start_chat_server()





