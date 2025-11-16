# udp_server.py
import socket

# 1. Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind the socket to a port
server_socket.bind(("127.0.0.1", 5000))

print("UDP Server is waiting for message...")

# 3. Receive message
data, addr = server_socket.recvfrom(1024)  # Buffer size = 1024 bytes

print("Received message:", data.decode())
print("From address:", addr)

# 4. Send a reply
reply = "Message received!"
server_socket.sendto(reply.encode(), addr)

server_socket.close()
