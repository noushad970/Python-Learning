# udp_client.py
import socket

# 1. Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Send a message to server
message = "Hello from client!"
client_socket.sendto(message.encode(), ("127.0.0.1", 5000))

# 3. Receive server's reply
data, server = client_socket.recvfrom(1024)

print("Reply from server:", data.decode())

client_socket.close()
