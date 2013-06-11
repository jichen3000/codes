import BaseHTTPServer

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('localhost', 9999)
    print "start server on localhost 9999"
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()