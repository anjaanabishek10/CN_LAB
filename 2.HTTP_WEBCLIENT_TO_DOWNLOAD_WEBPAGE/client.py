# ANJAAN ABISHEK - https://github.com/anjaanabishek10

import socket
url = str(input("\nEnter the URL of the webpage...\n"))
port = 10102000
request = "GET / HTTP/1.1\r\nHOST: {}\r\n\r\n".format(url).encode("utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((url,80))
s.send(request)
print("\n{}".format(s.recv(port).decode("utf-8")))
