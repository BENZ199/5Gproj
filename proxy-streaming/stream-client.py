import socket
import os

# Image streaming client settings
PROXY_HOST = 'tcp-proxy'  # The TCP proxy container name or IP
PROXY_PORT = 7654

# Path to the image you want to send
image_path = 'image.jpg'

# Check if the image exists
if not os.path.exists(image_path):
    print(f"Image file {image_path} not found!")
    exit(1)

# Open the image file
with open(image_path, 'rb') as f:
    # Create a socket to connect to the proxy
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((PROXY_HOST, PROXY_PORT))

    # Send the image data to the proxy
    print(f"Sending image to {PROXY_HOST}:{PROXY_PORT}...")
    data = f.read(1024)
    while data:
        client_socket.sendall(data)
        data = f.read(1024)

    print("Image sent successfully.")
    client_socket.close()
