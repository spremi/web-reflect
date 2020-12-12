#!/usr/bin/python
#
# web-reflect
#
# Copyright (c) 2020, Sanjeev Premi.
#


from argparse import ArgumentParser
from http.server import HTTPServer, BaseHTTPRequestHandler

AllowCors = False

IsDebug = False


class ReflectServer(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200, "ok")

        if (IsCors):
            self.send_header('Access-Control-Allow-Origin', '*')

        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

        self.end_headers()

    def do_GET(self):
        self.__ret_success('')

    def do_POST(self):
        self.__ret_success('')

    def do_PUT(self):
        self.__ret_success('')

    def do_DELETE(self):
        self.__ret_success('')

    def __ret_success(self, arg: str):
        '''
        Common function to return success response.
        '''
        self.send_response(200)

        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write(arg.encode('utf-8'))


if __name__ == '__main__':
    parser = ArgumentParser(
        description='web-reflect: A simple HTTP reflect server.')

    parser.add_argument('-b', '--bind', default='localhost',
                        type=str, help='Host name/address to bind.')

    parser.add_argument('-p', '--port', default=5500,
                        type=int, help='Port to listen.')

    parser.add_argument('-c', '--cors', default=False,
                        action='store_true', help='Enable CORS.')

    parser.add_argument('-d', '--debug', default=False,
                        action='store_true', help='Show debug messages.')

    args = parser.parse_args()

    host = args.bind
    port = args.port

    IsDebug = args.debug
    IsCors = args.cors

    print(f'Listening on http://{host}:{port}')
    print(f' - CORS  is {IsCors}')
    print(f' - Debug is {IsDebug}')

    reflect = HTTPServer((host, port), ReflectServer)

    reflect.serve_forever()
