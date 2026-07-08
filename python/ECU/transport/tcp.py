import socket
from .transport import Transport


class TCPTransport(Transport):

    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def connect(self):
        pass

    def write(self, data: bytes):
        self.sock.sendall(data)

    def read(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()