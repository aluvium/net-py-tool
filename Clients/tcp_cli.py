import socket 
T_HOST="10.66.121.1"
T_PORT=24240
#define client and connect to host
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((T_HOST,T_PORT))
#header data --> hes to be in bytes
payload=bytes("GET / HTTP/1.1\r\nUser-Agent: MS-DOS/2.0\r\n\r\n", "utf-8")
client.send(payload)
# recive data
response=client.recv(4096).decode('utf-8')
print(response)
