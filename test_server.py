import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))
server_socket.listen(1)
print("Server listening on port 8080...")
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")
