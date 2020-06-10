#
# simple web server running on Rapberry Pi.
# when request received at http port, send a message to screen
#
import socket
import sys

BIND_HOST = "0.0.0.0"
BIND_PORT = "80"

linz_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    linz_socket.bind((BIND_HOST, BIND_PORT))
except socket.error:
    print("Bind failure")
    sys.exit()

linz_socket.listen(5)

while True:
    client_socket, client_addr = linz_socket.accept()

    data = client_socket.recv(1024)
    if not data:
        break

    print('\nGot a request!')
    print(data)

    #http_response = b"\HTTP/1.1 200 OK "
    #client_socket.sendall(http_response)

client_socket.close()
linz_socket.close()
