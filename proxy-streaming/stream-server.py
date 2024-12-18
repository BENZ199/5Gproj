import socket

# Image streaming server settings
HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 7655

# Create a server socket to listen for incoming image streams
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Image streaming server listening on {HOST}:{PORT}...")

while True:
    # Accept a connection from the proxy
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive and save the incoming image stream
    with open('received_image.jpg', 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
        print("Image received and saved.")

    client_socket.close()
