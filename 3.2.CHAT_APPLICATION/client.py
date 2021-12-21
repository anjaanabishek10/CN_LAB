# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
client_message = ""
server_address = ("localhost", 1010)
recv_port = 10102000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print("\nConnected to {}\n".format(server_address))
while client_message != "end":
    client_message = str(input("Client: "))
    client_socket.send(client_message.encode("utf-8"))
    print("Server: {}".format(client_socket.recv(recv_port).decode("utf-8")))
