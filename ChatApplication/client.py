import socket
import threading

SERVER_IP = "127.0.0.1"
SERVER_PORT = 6000

def listen_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            print("\nFriend:", message)
        except:
            print("\nDisconnected from server")
            sock.close()
            break

def start_chat_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    print("Connected to chat server")
    print("Type 'exit' to leave\n")

    threading.Thread(target=listen_messages, args=(client,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "exit":
            client.close()
            break
        client.send(msg.encode())

start_chat_client()

