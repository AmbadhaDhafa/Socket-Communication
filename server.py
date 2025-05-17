import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9000))
server_socket.listen()
print('Listening on port 9000...')

while True:
    client_socket, address = server_socket.accept()
    print(f'Connection from {address} has been established!')
    client_socket.send(bytes("welcome to the server!", "utf-8"))
    client_socket.close()