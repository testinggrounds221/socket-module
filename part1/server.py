import socket

# Initialising Server Constants
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 64
FORMAT = "utf-8"

#Binding Server and Port as a single Tuple -> Address
ADDR = (SERVER, PORT)

# Staring Server
server = socket.socket()
server.bind(ADDR)

server.listen()
print(f"Server is running on {SERVER}")

while True:
    conn, addr = server.accept()  # conn -> connection Object, blocking point
    print(f"[NEW CONNECTION] from {addr[0]} connected at port {addr[1]}")
    while True:
        message = conn.recv(HEADER)
        if message:
            message = message.decode(FORMAT)
            print(message)
            conn.send("Message Received".encode(FORMAT))
