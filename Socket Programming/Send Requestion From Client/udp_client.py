# udp_client.py
import socket

# 1. Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Contact server by sending a message
message = "Hello Server!"
client_socket.sendto(message.encode(), ("127.0.0.1", 5000))

# 3. Wait for server reply
data, server = client_socket.recvfrom(1024)

print("Server replied:", data.decode())

client_socket.close()
