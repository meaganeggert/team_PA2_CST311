# udp_pinger_server_starter.py
# We will need the following module to generate
# randomized lost packets
import random
from socket import socket, AF_INET, SOCK_DGRAM

# TODO: 
# 1. Create a UDP socket. Be sure to use SOCK_DGRAM since we are working with UDP packets
# 2. Assign IP address and port number to socket
# 3. Initialze a variable to count the number of pings

def main():
    # TODO:
    # 1. Start an infinite loop
    # 2. Count the pings received using the previously initialized variable
    # 3. Generate a random number between 1 and 10 (inclusive)
    # 4. Receive the client packet along with the address it is coming from
    # 5. IF conditions for packet loss simulation are met, THEN consider the packet lost and do not respond
    # 6. Otherwise, the server responds

if __name__ == "__main__":
  main()

# The server sits in an infinite loop listening for incoming UDP packets. 
# When a packet comes in, the server will decide to respond based on the implemented packet loss simulation condition.
