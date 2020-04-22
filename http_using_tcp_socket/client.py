import sys
import socket

ADDRESS = ('localhost', 8000)
BUFF_SIZE = 1024

if len(sys.argv) < 4:
    print('Usage: client.py server_host server_port filename\n\t example: python client.py localhost 8000 test.html')
    exit()

host = sys.argv[1]
port = sys.argv[2]
filename = sys.argv[3]  # The arguments supplied in the command line
header = """GET /{} HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us
Host: {}""".format(filename, port)

main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_sock.connect(ADDRESS)
main_sock.sendall(header.encode())

result = ""  # result is store the response bytes
response = main_sock.recv(BUFF_SIZE)  # receive the response in 1Kb sections
while response:
    result += response.decode()
    response = main_sock.recv(BUFF_SIZE)

main_sock.close()
print('Received from the server:      ', result)
