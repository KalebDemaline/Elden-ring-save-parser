from http.server import HTTPServer, BaseHTTPRequestHandler
import tempfile
import os
import json
from Utils.Util import *

HOST = 'localhost'
PORT = 9999

temp: tempfile.TemporaryDirectory

class testHttp(BaseHTTPRequestHandler):

    def do_GET(self):
        global temp

        # with open(f'{temp.name}/save_file', 'rb') as f:
        with open('/Users/kalebsmac/Downloads/ER0000.sl2', 'rb') as f:
            file = f.read()

            if(isValidFile(file)):

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                self.wfile.write(bytes(json.dumps(getOwnedAndNot(file, 1), indent=4), 'utf-8'))

    def do_POST(self):
        global temp
        content_length = int(self.headers['Content-Length'])

        # Read the binary data sent by the client
        sent_save_file = self.rfile.read(content_length)

        if (isValidFile(sent_save_file)):
            temp = tempfile.TemporaryDirectory()
            os.chdir(temp.name)

            print(temp.name)

            with open('save_file', "wb") as f:
                    f.write(sent_save_file) 

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b"Data received successfully.")

def run():
    global temp
    print(f'Server running on port {PORT}')
    server = HTTPServer((HOST, PORT), testHttp)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        temp.cleanup()
        server.server_close()

if __name__ == '__main__':
    run()