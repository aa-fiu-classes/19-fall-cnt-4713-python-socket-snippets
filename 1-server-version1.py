#!/usr/bin/env python3

# Creating the socket
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

sock.bind((HOST, PORT))
sock.listen(5)
print('Waiting for incoming connections on', sock)
conn, addr = sock.accept()  # will block
print('Connected by', addr)
while True:
    data = conn.recv(1024) # will block and return buffer;
                           # 'None' if something bad happens
    if not data:
        break
    conn.send(data)
conn.close() # close the client socket (for talking to client)

sock.close() # close the server socket (for listening)
