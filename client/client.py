import socket
import sys

HOST, PORT = 

def send_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST,PORT))
        sock.send(bytes(command + "\n", "utf-8"))

    return sock.recv(1024)




