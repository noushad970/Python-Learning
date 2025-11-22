#!/usr/bin/env python3
"""
Concurrent file server (TCP). For each client:
- receive filename (utf-8, newline-terminated)
- spawn a thread for that client, passing filename as an argument
- thread sends file in chunks <= 1000 bytes, sleeping 200 ms after each chunk
"""


import contextlib
import socket
import threading
import time
import os

HOST = "0.0.0.0"    # listen on all interfaces
PORT = 9000         # pick any available port

CHUNK_SIZE = 1000   # bytes per flush operation
SLEEP_AFTER_CHUNK = 0.2  # 200 milliseconds

def client_file_sender(filename: str, client_sock: socket.socket, client_addr):
    """
    Thread target: sends the file 'filename' to the connected client socket.
    filename is passed as argument to the thread constructor (per requirement).
    """
    try:
        print(f"[{threading.current_thread().name}] Started for {client_addr} -> requested file: '{filename}'")
        # Validate filename to avoid directory traversal - optionally enforce a directory
        # Here we only allow files from server's working directory (no absolute or parent paths)
        if os.path.isabs(filename) or ".." in filename.replace("\\", "/"):
            raise ValueError("Invalid filename requested.")
        if not os.path.exists(filename) or not os.path.isfile(filename):
            msg = f"ERROR: File '{filename}' not found.\n"
            client_sock.sendall(msg.encode('utf-8'))
            print(f"[{threading.current_thread().name}] File not found: {filename}")
            return

        with open(filename, "rb") as f:
            while True:
                chunk = f.read(CHUNK_SIZE)
                if not chunk:
                    break
                client_sock.sendall(chunk)   # send chunk
                # sleep for 200 ms after each flush
                time.sleep(SLEEP_AFTER_CHUNK)
        # Optionally indicate EOF explicitly (but closing socket is enough)
        print(f"[{threading.current_thread().name}] Finished sending '{filename}' to {client_addr}")
    except Exception as e:
        print(f"[{threading.current_thread().name}] Error: {e}")
        with contextlib.suppress(Exception):
            err_msg = f"ERROR: {str(e)}\n"
            client_sock.sendall(err_msg.encode('utf-8'))
    finally:
        with contextlib.suppress(Exception):
            client_sock.shutdown(socket.SHUT_RDWR)
        client_sock.close()
        print(f"[{threading.current_thread().name}] Connection closed for {client_addr}")


def handle_connection(conn_sock: socket.socket, addr):
    """
    Read filename from client, then create a thread passing the filename as argument.
    The thread will handle the file transfer from that point on.
    """
    try:
        # Receive filename. We'll read until newline or small timeout
        conn_sock.settimeout(5.0)
        data = b""
        while True:
            part = conn_sock.recv(256)
            if not part:
                break
            data += part
            if b'\n' in data:
                break
        if not data:
            print(f"[main] No filename received from {addr}. Closing connection.")
            conn_sock.close()
            return
        # Extract filename (strip newline & spaces)
        filename = data.split(b'\n', 1)[0].decode('utf-8', errors='ignore').strip()
        # Create thread, passing filename as argument (and also pass client socket)
        t = threading.Thread(target=client_file_sender, args=(filename, conn_sock, addr), daemon=True)
        t.start()
        # DO NOT close conn_sock here — thread owns it now.
    except Exception as e:
        print(f"[main] Error while handling connection from {addr}: {e}")
        with contextlib.suppress(Exception):
            conn_sock.close()


def run_server(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"[main] Server listening on {host}:{port}")
        try:
            while True:
                conn, addr = s.accept()
                print(f"[main] Accepted connection from {addr}")
                # handle_connection will receive the filename and spawn thread to send
                # We call handle_connection in a separate thread to avoid blocking accept() while reading filename
                threading.Thread(target=handle_connection, args=(conn, addr), daemon=True).start()
        except KeyboardInterrupt:
            print("\n[main] Server shutting down (KeyboardInterrupt).")


if __name__ == "__main__":
    run_server()
