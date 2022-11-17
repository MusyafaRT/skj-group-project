import json
import socketserver
import sys
import threading

from data import CplanDataSession


class CplanRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        """Handle incoming connection and parse command"""
        thread_name = threading.current_thread().name
        command = self.request.recv(1024).decode().strip()
        print(f'{thread_name} received command {command}')
        command, *args = command.split()
        ses = CplanDataSession('cplan_data.txt')

        ok = False
        if command == 'list':
            ok = self.handle_list(ses, args)
        elif command == 'add':
            ok = self.handle_add(ses, args)
        elif command == 'del':
            ok = self.handle_del(ses, args)

        if ok:
            self.request.sendall(b'OK')
        elif ok is False:
            self.request.sendall(b'ERROR')

    def handle_list(self, ses, args):
        """Handle the `list` command"""
        data = ses.get_data()
        if not data:
            self.request.send('EMPTY')
        for date, desc in data:
            date = ses.date_to_str(date)
            res = f'{date} {desc}\n'.encode()
            self.request.send(res)

    def handle_add(self, ses, args):
        """Handle the `add` command"""
        if len(args) < 2:
            return False

        date = args[0]
        desc = ' '.join(args[1:])

        try:
            date = ses.str_to_date(date)
        except ValueError:
            return False

        ses.add(date, desc)
        ses.commit()
        return True

    def handle_del(self, ses, args):
        """Handle the `del` command"""
        if len(args) < 2:
            return False

        date = args[0]
        keyword = ' '.join(args[1:])

        try:
            date = ses.str_to_date(date)
        except ValueError:
            return False

        ses.remove(date, keyword)
        ses.commit()
        return True


class CplanServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """TCP server with ThreadingMixIn"""
    allow_reuse_address = True


def main(host, port):
    """Entry point for the server program"""
    server = CplanServer((host, port), CplanRequestHandler)
    with server:
        ip, port = server.server_address
        print(f'Cplan server running on {ip}:{port}')
        server.serve_forever()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <host> <port>')
        sys.exit(2)
    main(sys.argv[1], int(sys.argv[2]))
