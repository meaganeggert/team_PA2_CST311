import random
import socket


HOST = "10.0.0.1"
PORT = 3737

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Server listening on {}:{}'.format(HOST, PORT))
        while True:
            data, addr = s.recvfrom(1024)
            if not data:
                break
            message = data.decode('utf-8')
            message = message.upper()
            data = message.encode('utf-8')
            s.sendto(data, addr)

        


if __name__ == "__main__":
  main()
