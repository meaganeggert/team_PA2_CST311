# udp_pinger_server_starter.py
# We will need the following module to generate
# randomized lost packets
import random
import time
from socket import socket, AF_INET, SOCK_DGRAM



# 1. Create a UDP socket. Be sure to use SOCK_DGRAM since we are working with UDP packets
# 2. Assign IP address and port number to socket
# 3. Initialze a variable to count the number of pings
s = socket(AF_INET, SOCK_DGRAM)
HOST = "10.0.0.1"
PORT = 2500
MAX_PACKET_COUNT = 10
# ***Initialized ping count within main***



# Define which packets are going to be dropped
def packet_drop_order():
   tmpArray = []

   # For 40 percent of expected packets to be recieved, determine which packets will be dropped.
   for x in range(int(.4 * MAX_PACKET_COUNT)):
      # Range starts at two because we don't want the first packet to be dropped.
      rndNum = random.randint(2,MAX_PACKET_COUNT)

      # Make sure there are no repeats in selected packets
      while rndNum in tmpArray:
         rndNum = random.randint(2,MAX_PACKET_COUNT)
       
      tmpArray.insert(x, rndNum)
   print("Packets to be dropped: {}".format(tmpArray))
   return tmpArray




# Determine if packet should drop or not
def packet_drop_valid(ping_count, packet_drops):
   # If ping count matches predetermined packets to be dropped, return true
   if ping_count in packet_drops:
      return True
   # Any other scenarios we will not drop packet
   return False




def main():
    # Set up socket and initialize ping count and packets to be dropped
    print("Initializing")
    s.bind((HOST, PORT))
    ping_count = 0
    print("Server listening on {HOST}:{Port}")

    while True:
       # Retrieve data from client, must be re-encoded later
       data, addr = s.recvfrom(1024)
       message = data.decode()
       
       # If client reset ping count, server should reset ping count and order of packet drops
       if message == "Ping1":
          ping_count = 0
          packet_drops = packet_drop_order()

       # Otherwise, keep incrementing the ping counter and re-encoding the data
       ping_count += 1
       data = message.encode('utf-8')
       
       # Determine if the server should respond to the client
       if not data or packet_drop_valid(ping_count, packet_drops):
          print("Packet dropped")
       else:
          print("Packet recieved")
          s.sendto(data, addr)




if __name__ == "__main__":
  main()

# The server sits in an infinite loop listening for incoming UDP packets. 
# When a packet comes in, the server will decide to respond based on the implemented packet loss simulation condition.