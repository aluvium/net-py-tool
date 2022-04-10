import socket 
T_HOST="example.com"
T_PORT=80
#define client and connect to host
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((T_HOST,T_PORT))

#header data --> hes to be in bytes
info=bytes("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n", "utf-8")
client.send(info)

# recive data
response=client.recv(4096)
print(response)
