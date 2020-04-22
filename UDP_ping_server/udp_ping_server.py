import random
import socket

ADDRESS = ('localhost', 8000)
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDRESS)

while True:
    data, address = sock.recvfrom(BUFF_SIZE)  # Receive data from client
    if random.randint(0, 100) < 20:  # Simulate package loss with 20% probability
        continue
    sock.sendto(data, address)  # Respond to client
