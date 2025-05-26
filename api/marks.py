from http.server import BaseHTTPRequestHandler
import json
import os
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Load student data with correct filename
            json_path = os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')
            with open(json_path) as f:
                students = json.load(f)
            
            # Get query parameters
            query = parse_qs(urlparse(self.path).query)
            names = query.get('name', [])
            
            # Get marks for requested names
            marks = [students.get(name, 0) for name in names]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            self.wfile.write(json.dumps({"marks": marks}).encode())
            
        except Exception as e:s
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode())