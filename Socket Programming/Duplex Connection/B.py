# B.py - Full Duplex UDP (Process B)
import socket
import threading

# --------- RECEIVER FUNCTION ---------
def receive_messages():
    recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recv_socket.bind(("127.0.0.1", 6000))
    
    print("[B] Receiver ready on port 6000...")

    while True:
        data, addr = recv_socket.recvfrom(1024)
        print(f"[B] Received from A: {data.decode()}")

# --------- SENDER FUNCTION ---------
def send_messages():
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        msg = input("[B] Enter message for A: ")
        send_socket.sendto(msg.encode(), ("127.0.0.1", 5000))

# --------- START THREADS ---------
threading.Thread(target=receive_messages, daemon=True).start()
send_messages()
