import socket
import time

HOST = "10.0.0.1"  
PORT = 2500
TIMEOUT = 1.0 
NUM_PINGS = 10 

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.settimeout(TIMEOUT)
    
    # initialize values
    min_rtt = float('inf')
    max_rtt = float('-inf')
    total_rtt = 0
    ping_count = 0
    lost_count = 0

    while ping_count < NUM_PINGS:
        ping_count += 1
        message = "Ping{}".format(ping_count)
        byte_msg = message.encode('utf-8')
        start_time = time.time()

        try:
            # send the signal
            s.sendto(byte_msg, (HOST, PORT))

            # wait for the reply
            data = s.recvfrom(1024)
            end_time = time.time()

            # calculate RTT
            rtt = (end_time - start_time) * 1000
            
            # update RTT stats
            total_rtt += rtt
            if rtt < min_rtt:
                min_rtt = rtt
            if rtt > max_rtt:
                max_rtt = rtt
            
            print("Ping {}: rtt = {:.3f} ms".format(ping_count, rtt))

        except socket.timeout:
            lost_count += 1
            print("Ping {}: Request timed out".format(ping_count))

    # calculate values
    if NUM_PINGS - lost_count > 0:
        avg_rtt = total_rtt / (NUM_PINGS - lost_count)
    
    loss_rate = (lost_count / NUM_PINGS) * 100

    # print summary values
    print("\nSummary values:")
    print("min_rtt = {:.3f} ms".format(min_rtt))
    print("max_rtt = {:.3f} ms".format(max_rtt))
    print("avg_rtt = {:.3f} ms".format(avg_rtt))
    print("Packet loss: {:.2f}%".format(loss_rate))