import random
import socket


HOST = "10.0.0.1"
PORT = 3737

def main():
    expected_sequence_number = 1  # Start with the first expected sequence number
    report_filename = None  # Will be initialized based on the first client connection

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f'Server listening on {HOST}:{PORT}')
        
        while True:
            data, addr = s.recvfrom(1024)
            if not data:
                break
            
            # Extract client IP for the filename
            client_ip = addr[0]
            if report_filename is None:
                report_filename = f"server_hb_report_{client_ip}.txt"
                print(f"Writing report to {report_filename}")

            # Decode the received message
            message = data.decode('utf-8')

            # MEAGAN DEBUGGING
            message = message.upper()
            data = message.encode('utf-8')
            s.sendto(data, addr)

            try:
                # Parse the sequence number and timestamp from the message
                parts = message.split()
                received_sequence_number = int(parts[0])  # Sequence number
                received_timestamp = parts[1]  # Timestamp in HH:MM:SS format
            except (IndexError, ValueError):
                # Skip processing if the message format is not as expected
                print(f"Received unexpected message format: {message}")
                continue
            

            # Open report file in append mode
            with open(report_filename, "a") as report_file:
                # Handle missing heartbeats
                while expected_sequence_number < received_sequence_number:
                    # Log missing heartbeat to the report
                    report_file.write(f"HB {expected_sequence_number}: Missing UDP heartbeat\n")
                    print(f"HB {expected_sequence_number}: Missing UDP heartbeat")
                    expected_sequence_number += 1

                # Log the received heartbeat to the report
                report_file.write(f"HB {received_sequence_number}: Messages received: sequence {received_sequence_number}, time {received_timestamp}\n")
                print(f"HB {received_sequence_number}: Messages received: sequence {received_sequence_number}, time {received_timestamp}")

                # Update the expected sequence number
                expected_sequence_number = received_sequence_number + 1

if __name__ == "__main__":
    main()
