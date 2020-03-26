#!/usr/bin/env python3

import socket

HOST, PORT = "localhost", 65432

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server
    sock.connect((HOST, PORT))

    # Receive initial information from server side
    received = sock.recv(1024)
    print("Received: {0}".format(received))

    # while True:
    # Send something
    data = input("What do you want to send?:")
    sock.sendall(data.encode())
    # waiting for the server response
    received = sock.recv(1024)
    print("Received: {0}".format(received))
