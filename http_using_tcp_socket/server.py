import socket

ADDRESS = ('localhost', 8000)
BUFF_SIZE = 1024
NOT_FOUND_RESPONSE = '\nHTTP/1.1 404 Not Found\n\n'
OK_RESPONSE = """HTTP/1.1 200 OK
Server: Ahmad12
Content-Type: text/html
"""

main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_sock.bind(ADDRESS)
main_sock.listen(1)  # accept only one request

while True:
    sock, address = main_sock.accept()  # establish the connection
    req = sock.recv(BUFF_SIZE)
    file_name = req.split()[1][1:]  # Extract file from the request
    try:
        # Open the file
        file = open(file_name.decode(), 'rb')

        # Send OK header
        sock.sendall(OK_RESPONSE.encode())
        # Send the file KB to KB
        response = file.read(BUFF_SIZE)
        while response:
            sock.sendall(response)
            print(repr(response), 'was sent to client.')
            response = file.read(BUFF_SIZE)
        # file.close()
    except IOError as e:
        print('File not found, responding with 404 code.')
        sock.sendall(NOT_FOUND_RESPONSE.encode())

    #  Chrome sends extra requests which we ignore
    if req.decode().__contains__('Chrome'):
        req = sock.recv(BUFF_SIZE)
        print('Extra request: ', req)
    sock.close()
