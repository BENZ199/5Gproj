import socket

# VM public IP and port
LISTEN_HOST = '0.0.0.0'  # Listen on all available interfaces (0.0.0.0 binds to all)
LISTEN_PORT = 7654

# Image streaming server IP and port
FORWARD_HOST = '100.27.44.103'  # Image streaming server IP
FORWARD_PORT = 7654  # Port for the image streaming server

# Create a server socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((LISTEN_HOST, LISTEN_PORT))
server_socket.listen(5)
print(f"Listening for incoming connections on {LISTEN_HOST}:{LISTEN_PORT}...")

while True:
    # Accept an incoming connection from UE
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Create a socket to connect to the image streaming server
    forward_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    forward_socket.connect((FORWARD_HOST, FORWARD_PORT))

    # Forward data between the client (UE) and the image streaming server
    try:
        while True:
            # Receive data from the client (UE)
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Forwarding data to {FORWARD_HOST}:{FORWARD_PORT}")
            forward_socket.sendall(data)

            # Receive data from the image streaming server
            response = forward_socket.recv(1024)
            if not response:
                break
            print(f"Sending response back to client {client_address}")
            client_socket.sendall(response)
    except Exception as e:
        print(f"Error during forwarding: {e}")
    finally:
        # Close both client and forward connections
        client_socket.close()
        forward_socket.close()

