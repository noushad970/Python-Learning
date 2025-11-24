#!/usr/bin/env python3
"""
Simple file client to request a file from the server.
Usage:
    python file_client.py <server_host> <server_port> <remote_filename>
Saves received data to: downloaded_<remote_filename>
"""

import socket
import sys
import os

def download_file(server_host, server_port, remote_filename):
    out_name = f"downloaded_{os.path.basename(remote_filename)}"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        # Send filename + newline as protocol
        s.sendall((remote_filename + "\n").encode('utf-8'))
        # Receive until socket closes
        with open(out_name, "wb") as f:
            while True:
                if data := s.recv(4096):
                    f.write(data)
                else:
                    break
    print(f"[client] Download saved as '{out_name}'")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python file_client.py <server_host> <server_port> <remote_filename>")
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    download_file(host, port, filename)
