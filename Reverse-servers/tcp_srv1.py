import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.ack=b"""This is a data. For sending from server.
        ACK!"""
        print("[x] {} wrote:".format(self.client_address[0]))    
        print(self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())
        self.request.sendall(self.ack)
        

if __name__ == "__main__":
    HOST, PORT = "localhost", 24240
    # Create the server, binding to localhost on port 24240
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        print("[x] Listening on %s : %d" % (HOST,PORT))
        server.serve_forever()
