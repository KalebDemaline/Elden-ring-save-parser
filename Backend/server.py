from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import cgi
import glob
import json
import os
from Utils.Util import *

HOST = 'localhost'
PORT = 9999


class testHttp(BaseHTTPRequestHandler):

    def do_GET(self):
        path = urlparse(self.path).path
        query_components = parse_qs(urlparse(self.path).query)

        if path == '/names':
            self.get_names(query_components)
        elif path == '/read':
            self.get_file(query_components)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

    def get_file(self, query_components):
        user_id = query_components.get('user_id', [None])[0]
        character_index = query_components.get('character_index', [None])[0]

        print(user_id, character_index)

        if user_id is None:
            return

        pattern = os.path.join('SaveFiles', f'{user_id}_save*')

        found_file = glob.glob(pattern)
        if found_file:
            with open(found_file[0], 'rb') as f:
                file = f.read()

                if (isValidFile(file)):

                    self.send_response(200)
                    self.send_header("Content-type", "application/json")
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()

                    self.wfile.write(bytes(json.dumps(getOwnedAndNot(file, int(character_index)), indent=4), 'utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

    def get_names(self, query_components):
        user_id = query_components.get('user_id', [None])[0]
        character_index = query_components.get('character_index', [None])[0]

        print(user_id, character_index)

        if user_id is None:
            return

        pattern = os.path.join('SaveFiles', f'{user_id}_save*')

        # Use glob to find files matching the pattern
        found_file = glob.glob(pattern)
        if found_file:
            with open(found_file[0], 'rb') as f:
                file = f.read()

                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                self.wfile.write(bytes(json.dumps(getNames(file), indent=4), 'utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
   
    def do_POST(self):
        # Parse the form data posted
        content_type, pdict = cgi.parse_header(self.headers['content-type'])

        if content_type == 'multipart/form-data':
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            pdict['CONTENT-LENGTH'] = int(self.headers['content-length'])

            fields = cgi.parse_multipart(self.rfile, pdict)
            user_id = fields.get('user_id')[0]
            sent_save_file = fields.get('save_file')[0]

            print(user_id)

        if (isValidFile(sent_save_file)):
            with open(f"SaveFiles/{user_id}_save", 'wb') as temp_file:
                temp_file.write(sent_save_file)

            # Send response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(bytes(f"{1}", "utf-8"))

def delete_save_files(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: The path {directory_path} is not a valid directory.")
        return

    # Pattern to match all files in the directory
    pattern = os.path.join(directory_path, '*')

    # Use glob to find all files matching the pattern
    for file_path in glob.glob(pattern):
        if os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

def run():
    print(f'Server running on port {PORT}')
    server = HTTPServer((HOST, PORT), testHttp)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        delete_save_files('SaveFiles')
        server.server_close()


if __name__ == '__main__':
    run()
