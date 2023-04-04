from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer,
)

import sys


class UtilsMixin:

    def get_hostname(self):
        return 'localhost'

    def get_port(self):
        try:
            server_port = None
            for idx,arg in enumerate(sys.argv):
                if server_port is None:
                    server_port = sys.argv[idx+1] if arg == '--port' else None
                else:
                    server_port = int(server_port)
            if server_port is None:
                raise
        except:
            server_port = 8080
        finally:
            return server_port


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


class Main(UtilsMixin):

    def __init__(self):
        self.hostname = self.get_hostname()
        self.server_port = self.get_port()
        self.web_server = HTTPServer((self.hostname, self.server_port), MyServer)

    def run_server(self):
        print(f"Server started in http://{self.hostname}:{self.server_port}")

        try:
            self.web_server.serve_forever()
        except KeyboardInterrupt:
            self.web_server.server_close()
            print("Server stopped.")


if __name__ == "__main__":
    main = Main()
    main.run_server()