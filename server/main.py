import sys
import socketserver
import threading


class CplanRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        self.request.sendall()


class CplanServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main(host, port):
    server = CplanServer((host, port), CplanRequestHandler)
    with server:
        ip, port = server.server_address
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.start()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <host> <port>')
        sys.exit(2)
    main(int(sys.argv[1]), int(sys.argv[2]))
