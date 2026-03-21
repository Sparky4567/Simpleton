import http.server
import socketserver
from settings import DEFAULT_PORT
PORT = 3001

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", DEFAULT_PORT), Handler) as httpd:
	try:
		print(f"Serving at port {DEFAULT_PORT}\n\n")
		print(f"Serving on http://0.0.0.0:{DEFAULT_PORT} or http://127.0.0.1:{DEFAULT_PORT}\n\n")
		httpd.serve_forever()
	except KeyboardInterrupt as e:
		print("\nExiting gracefully\n")
		quit()
