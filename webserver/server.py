from http.server import SimpleHTTPRequestHandler, HTTPServer

# Set the directory where our HTML files are located
directory = 'app'

# Set up the server
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Start the server
print("Starting server on port 8000...")
httpd.serve_forever()
