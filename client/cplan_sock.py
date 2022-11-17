import socket
import sys


def send_command(host, port, command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        sock.send(bytes(command + "\n", "utf-8"))
        buf = b''
        while True:
            data = sock.recv(4096)
            if not data:
                break
            buf += data
        return buf.decode()

