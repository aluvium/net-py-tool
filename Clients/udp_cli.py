import socket
import sys

HOST, PORT = "10.66.121.1", 24240
payload = "Stream: DATA"

# SOCK_DGRAM is the socket type to use for UDP sockets
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(payload, "utf-8"), (HOST, PORT))
received = str(sock.recv(1024), "utf-8")

print(f"Sent:     {payload}")
print(f"Received: {payload}")
