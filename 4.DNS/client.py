# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
server_address = ("localhost", 1010)
recv_port = 1020
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
domain = str(input("Enter domain\n"))
client_socket.sendto(domain.encode("utf-8"),server_address)
ip_data, server_address = client_socket.recvfrom(recv_port)
ip_data = ip_data.decode("utf-8")
print(ip_data)