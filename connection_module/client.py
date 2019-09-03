import selectors
from . import servicer

class Client:
    def __init__(self, addr):
        self.addr = addr
        self.inb = b'' # input buffer
        self.outb = b'' # output buffer

    @staticmethod
    def acceptConnection(sock, sel):
        conn, addr = sock.accept()  # Should be ready to read
        print('accepted connection from', addr)
        conn.setblocking(False)
        self = Client(addr)

        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        selKey = sel.register(conn, events, data=self)
        return self, selKey

    def serviceConnection(self, *kargs, **kwargs):
        servicer.serviceConnection(kargs, **kwargs)
