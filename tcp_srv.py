import socket
import threading

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BIND_IP = "0.0.0.0"
BIND_PORT = 24240
SERVER.bind((BIND_IP, BIND_PORT))
SERVER.listen(3)
print("[#] Listening on: %s:%d" % (BIND_IP, BIND_PORT))
# This is the thread we handle the data from  the client

def handle_client(client_socket):
    # show the data from the client
    request = client_socket.recv(1024)
    print("[#] Received: %s" % request)
    # Return a packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = SERVER.accept()
    print ("[#] Accepted connection from: %s:%d" % (addr[0], addr[1]))
    # activate the function to handle the data from client
    client_handler = threading.Thread(target = handle_client, args=(client,))
    client_handler.start()

