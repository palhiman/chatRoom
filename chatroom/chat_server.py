# chat room connection -- client->client

import threading
import socket

host = "127.0.0.1"
port = 4499

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

clients = [] # list for storing clients
aliases = [] # list for storing client alias's


# function for broadcasting messages to every clients
def broadcast(msg):
    for client in clients:
        client.send(msg)

# function to handle client's connections
def handle_clients(client):
    while True:
        try:
            msg = client.recv(1024) #
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"{alias} has left the chat room !!!". encode("utf-8"))
            aliases.remove(alias)
            break

# function to receive the clients connection
def receive():
    while True:
        print("[*] SERVER IS UP AND RUNNING ALSO LISTENING SILENTLY ...")

        client, address = server.accept()
        print(f"[**] Connection established successfully with {str(address)}")
        client.send("alias???".encode("utf-8"))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"Client's alias is {alias}".encode("utf-8"))
        broadcast(f"{alias} has connected to the chat room".encode("utf-8"))
        client.send("you are now connected !!!".encode("utf-8"))

        thread = threading.Thread(target=handle_clients, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()
