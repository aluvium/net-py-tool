import socket 

t_host="scanme.nmap.org"
t_port=80
#define client and connect to host
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((t_host,t_port))

#header data --> hes to be in bytes
info=bytes("GET / HTTP/1.1\r\nHost: scanme.nmap.com\r\n\r\n ", "utf-8")
client.send(info)

# recive data
response=client.recv(4096)

print(response)
