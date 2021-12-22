# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
server_message = ""
server_address = ("localhost", 1010)
recv_port = 1020
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()
print("\nWaiting for connection...")
client_socket, client_address = server_socket.accept()
print("\nConnected to {}\n".format(client_address))
while server_message != "end":
    print("Client: {}".format(client_socket.recv(recv_port).decode("utf-8")))
    server_message = str(input("Server: "))
    client_socket.send(server_message.encode("utf-8"))
