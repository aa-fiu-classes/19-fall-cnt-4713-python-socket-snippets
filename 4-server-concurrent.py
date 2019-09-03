#!/usr/bin/env python3

import selectors
import socket
from connection_module.client import Client

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind((HOST, PORT))
lsock.listen(10)
lsock.setblocking(False)

sel = selectors.DefaultSelector()
sel.register(lsock, selectors.EVENT_READ, data=None)

print('listening on', lsock.getsockname())
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            Client.acceptConnection(key.fileobj, sel)
        else:
            key.data.serviceConnection(key, mask, sel)
