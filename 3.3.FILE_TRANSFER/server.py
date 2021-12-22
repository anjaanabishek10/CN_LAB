# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import os
import socket
server_address = ("localhost", 1010)
recv_port = 1020
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()
print("\nWaiting for connection...")
client_socket, client_address = server_socket.accept()
print("\nConnected to {}\n".format(client_address))
file_name = client_socket.recv(recv_port).decode("utf-8")
check = str(os.path.exists(file_name))
if check == "True":
    print("Transfering file to client...\n")
    file = open(file_name, "r")
    data = file.read()
    client_socket.send(data.encode("utf-8"))
    file.close()
    print("Transfering completed")
else:
    client_socket.send("0".encode("utf-8"))
    print("\nNo such file exist")
