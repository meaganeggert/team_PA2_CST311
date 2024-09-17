import socket
import random
import time
from datetime import datetime

HOST = "10.0.0.1"  # todo: specify the server's hostname or IP address inside the quotes
PORT = 3737 # todo: specify the port number used by the server

HB_num = 1;

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    for i in range(10):
        now = datetime.now() # current date/time
        cur_time = now.strftime("%H:%M:%S")
#        cur_time = now.strftime("%H:%M:%S:%f") # This format includes microseconds

        drop_prob = random.random()
        if drop_prob > 0.3:
            message = str(HB_num) + " " + cur_time
            byte_msg = message.encode('utf-8')
            s.sendall(byte_msg)
            data = s.recv(1024)
            print("Received: {}".format(data.decode('utf-8')))
        # For debugging purposes
#        elif drop_prob <= 0.3:
#            message = "message dropped"
#            byte_msg = message.encode('utf-8')
#            s.sendall(byte_msg)
#            data = s.recv(1024)
#            print("Received: {}".format(data.decode('utf-8')))

        HB_num += 1
        time.sleep(3)
