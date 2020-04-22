import socket
import time

ADDRESS = ('localhost', 8000)
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)  # If server response takes more than one second, the packet is assumed lost

for i in range(10):  # ping the server 10 times
    send_time = time.time()
    sock.sendto("Hey, I'm Pinging you!!!".encode(), ADDRESS)
    try:
        sock.recvfrom(BUFF_SIZE)
        recv_time = time.time()
        print('The RTT is', recv_time - send_time)
    except socket.timeout:
        print('The package is lost...')
