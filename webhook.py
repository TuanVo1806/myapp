from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class Handler(BaseHTTPRequestHandler):
	def do_POST(self):
		if self.path=='/deloy':
			subprocess.call(['bash','/home/tuanvo/myapp/deloy.sh'])
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b'Deloy triggered')
		else:
			self.send_reponse(404)
			self.end_headers()

server=HTTPServer(('0.0.0.0',5000), Handler)
print("Listening on port 5000...")
server.serve_forever()
