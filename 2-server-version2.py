#!/usr/bin/env python3

# Creating the socket
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(5)

    print('Waiting for incoming connections on', sock)
    conn, addr = sock.accept() # will block
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # will block and return buffer;
                                   # 'None' if something bad happens
            if not data:
                break
            conn.send(data)
    # 'conn' will close automatically too

# 'sock' will close automatically when exiting 'with' block
