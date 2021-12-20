# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
message = str(input("\nEnter the message...\n"))
address = ("localhost", 1010)
port = 10102000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
s.send(message.encode("utf-8"))
print("\nMessage sent to server from client: {}".format(message))
print("Message received from server to client: {}\n".format(s.recv(port).decode("utf-8")))
