import http.server, socketserver

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200); self.end_headers(); self.wfile.write(b"ok")
        else:
            self.send_response(200); self.end_headers(); self.wfile.write(b"hello")

with socketserver.TCPServer(("0.0.0.0", 8080), H) as s:
    s.serve_forever()
