#!/usr/bin/python
#
# web-reflect
#
# Copyright (c) 2020, Sanjeev Premi.
#


from argparse import ArgumentParser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

import json


AllowCors = False

IsDebug = False


class ReflectServer(BaseHTTPRequestHandler):

    __response = dict()

    def do_OPTIONS(self):
        self.send_response(200, "ok")

        if (IsCors):
            self.send_header('Access-Control-Allow-Origin', '*')

        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

        self.end_headers()

    def do_GET(self):
        if self.path.startswith('/favicon'):
            self.__serve_favicon()
            return

        self.__ret_success()

    def do_POST(self):
        self.__get_content()
        self.__ret_success()

    def do_PUT(self):
        self.__get_content()
        self.__ret_success()

    def do_DELETE(self):
        self.__get_content()
        self.__ret_success()

    def __serve_favicon(self):
        '''
        Return favicon.
        '''
        self.send_response(200)
        self.send_header('Content-type', 'image/x-icon')
        self.end_headers()

        with open('content/favicon.png', 'rb') as f:
            self.wfile.write(f.read())

    def __init_response(self):
        '''
        Initialize attributes of the response.
        '''
        self.__response['method'] = self.command
        self.__response['from'] = self.address_string()
        self.__response['path'] = parse.urlparse(self.path).path

    def __get_query_params(self):
        '''
        Extract query params and add to the response.
        '''
        req_query = dict()

        query_params = parse.urlparse(self.path).query

        self.__response['query_string'] = query_params
        self.__response['query'] = parse.parse_qs(query_params)

    def __get_content(self):
        '''
        Extract content and add to the response.
        '''
        content_type = self.headers.get('Content-Type')
        content_length = self.headers.get('Content-Length')
        length = int(content_length) if content_length else 0

        content = self.rfile.read(length).decode("utf-8")

        if content_type == 'application/json':
            payload = json.loads(content)
        else:
            payload = content

        self.__response['payload'] = payload

    def __get_headers(self):
        '''
        Extract headers and add to the response.
        '''
        req_headers = dict()
        for n, v in sorted(self.headers.items()):
            req_headers[n] = v

        self.__response['headers'] = req_headers

    def __ret_success(self):
        '''
        Common function to return success response.
        '''
        self.__init_response()
        self.__get_headers()
        self.__get_query_params()

        self.send_response(200)

        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        resp = json.dumps(self.__response)

        self.wfile.write(resp.encode('utf-8'))

        #
        # Clear the dictionary contents.
        #
        if self.__response:
            self.__response.clear()


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
