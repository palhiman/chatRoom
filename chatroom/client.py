import socket
import threading

alias = input("Enter an alias for chat room > ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 4499))

# function for receiving  message from other clients through server
def client_receive():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8") # receive and decode 
            if msg == "alias???":
                client.send(alias.encode("utf-8"))
            else:print(msg)
        except:
            print("Error !!!")
            client.close()
            break

# function for sending message from other clients through server
def client_send():
    while True:
        msg = f'{alias}: {input(" ")}'
        client.send(msg.encode("utf-8"))
        

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()



