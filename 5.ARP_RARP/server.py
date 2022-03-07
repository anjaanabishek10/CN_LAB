# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
arp_table = {"1.1.1.1" : "aa:aa:aa:aa:aa:aa", "2.2.2.2" : "bb:bb:bb:bb:bb:bb", "3.3.3.3" : "cc:cc:cc:cc:cc:cc", "aa:aa:aa:aa:aa:aa" : "1.1.1.1", "bb:bb:bb:bb:bb:bb" : "2.2.2.2", "cc:cc:cc:cc:cc:cc" : "3.3.3.3"}
server_address = ("localhost", 1010)
recv_port = 1020
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen()
print("\nWaiting for connection...")
client_socket, client_address = server_socket.accept()
print("\nGot request from {}\n".format(client_address))
data = client_socket.recv(recv_port).decode("utf-8")
return_data = arp_table.get(data, "Given IP or MAC not found in ARP Table")
client_socket.send(return_data.encode("utf-8"))