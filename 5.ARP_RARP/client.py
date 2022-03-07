# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
server_address = ("localhost", 1010)
recv_port = 1020
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
print("\nConnected to {}\n".format(server_address))
choice = str(input("ARP or RARP\n"))
if choice == "ARP" :
    user_data = input("Enter IP\n")
    client_socket.send(user_data.encode("utf-8"))
elif choice == "RARP" :
    user_data = input("Enter MAC\n")
    client_socket.send(user_data.encode("utf-8"))
data = client_socket.recv(recv_port).decode("utf-8")
print(data)