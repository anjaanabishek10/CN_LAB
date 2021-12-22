# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
server_address = ("localhost", 1010)
recv_port = 1020
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print("\nConnected to {}\n".format(server_address))
file_name = str(input("Enter file name\n"))
client_socket.send(file_name.encode("utf-8"))
data = client_socket.recv(recv_port).decode("utf-8")
if data != "0":
    print("\nReceiving file from server...")
    file = open("client.txt", "w")
    file.write(data)
    file.close()
    print("\nFile received from server")
else:
    print("\nNo such file exist")
