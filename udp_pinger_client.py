## PROGRAM COPIED FROM PA1 TO BE MODIFIED TO SUIT PA2

# testing testing

import socket

HOST = "10.0.0.1"  # todo: specify the server's hostname or IP address inside the quotes
PORT = 3737 # todo: specify the port number used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    message = "ping"
    byte_msg = message.encode('utf-8')
    s.sendall(byte_msg)
        
    data = s.recv(1024)
    print("Received: {}".format(data.decode('utf-8')))
        
print("DONE")
