import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

FORMAT = "utf-8"
ADDR = (SERVER, PORT)
HEADER = 64

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while (True):
    message = input("Enter Message to be sent : ")
    message = message.encode(FORMAT)
    message += b" " * (64 - len(message))
    client.send(message)
    print(f"{client.recv(16).decode(FORMAT)} \n")