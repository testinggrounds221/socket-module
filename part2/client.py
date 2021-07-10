import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

FORMAT = "utf-8"
ADDR = (SERVER, PORT)
HEADER = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while (input("Send File ? : ")):

    filename = "txtFile.txt"
    file = open(filename, "rb")
    SendData = file.read()
    send_data_lenght = (str)(len(SendData)).encode(FORMAT)
    send_data_lenght += b" " * (HEADER - len(send_data_lenght))

    client.send(send_data_lenght)
    client.send(SendData)
    print(f"{client.recv(16).decode(FORMAT)} \n")
