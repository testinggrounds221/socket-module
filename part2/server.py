import socket
import datetime
# Initialising Server Constants
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 1024
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
        data_length = conn.recv(HEADER)
        if data_length:
            data_length = (int)(data_length.decode(FORMAT).strip())
            print(f"Receiving file of length {data_length}")
            received_file = conn.recv(data_length)
            conn.send("Message Received".encode(FORMAT))
            now = datetime.datetime.now()
            c_tm = now.strftime("%M_%S")
            file1 = open(f"rec_file{c_tm}.txt", "wb")
            file1.write(received_file)
            file1.close()
