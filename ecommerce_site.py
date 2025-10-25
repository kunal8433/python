# server.py
# Run this with: python server.py
import http.server
import socketserver
import os

PORT = 8000

# Set current directory to this file's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
print(f"🚀 Server running at http://localhost:{PORT}")
print("Press CTRL + C to stop")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
