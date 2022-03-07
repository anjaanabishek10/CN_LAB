# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
ip_table = {"www.google.com" : "1.1.1.1", "www.youtube.com" : "1.1.1.2", "www.gmail.com" : "1.1.1.3", "www.amazon.com" : "1.1.1.4", "www.flipkart.com" : "1.1.1.5", "www.facebook.com" : "1.1.1.6"}
server_address = ("localhost", 1010)
recv_port = 1020
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(server_address)
print("\nWaiting for connection...")
client_data, client_address = server_socket.recvfrom(recv_port)
print("\nGot IP request from {}\n".format(client_address))
data = client_data.decode("utf-8")
domain_ip = ip_table.get(data, "Given Domain not found in our DNS Table").encode("utf-8")
server_socket.sendto(domain_ip, client_address)