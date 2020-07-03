#!/usr/bin/python3
import os
import http.server
import socketserver


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


root_dir = '/home/leader/_work'
PORT = 8080


def run(server_class=ThreadedTCPServer, handler_class=http.server.SimpleHTTPRequestHandler, web_dir=root_dir,
        tcp_port=PORT):
    os.chdir(web_dir)
    server_address = ('', tcp_port)
    server_class.allow_reuse_address = True
    handler_class.extensions_map.update({
        '': 'text/plain; charset=UTF-8',
        '.py': 'text/plain; charset=UTF-8',
        '.sh': 'text/plain; charset=UTF-8',
        '.txt': 'text/plain; charset=UTF-8',
        '.js': 'text/plain; charset=UTF-8',
        '.xspf': 'text/plain; charset=UTF-8',
        '.bin': 'application/octet-stream; charset=UTF-8',
        '.otz': 'application/octet-stream; charset=UTF-8',
    })
    with server_class(server_address, handler_class) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    run()
