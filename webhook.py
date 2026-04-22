from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class Handler(BaseHTTPRequestHandler):
	def do_POST(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write(b'Webhook is rungning')

server=HTTPServer(('0.0.0.0',5000), Handler)
print("Listening on port 5000...")
server.serve_forever()
