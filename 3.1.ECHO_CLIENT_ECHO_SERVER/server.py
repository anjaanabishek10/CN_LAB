# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
address = ("localhost", 1010)
port = 10102000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen()
print("\nWaiting for connection...")
client, client_address = s.accept()
print("\nConnection established on {}".format(client_address))
message = client.recv(port)
print("Message received from client to server: {}\n".format(message.decode("utf-8")))
client.send(message)

