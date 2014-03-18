import SimpleHTTPServer
import BaseHTTPServer
import CGIHTTPServer

BaseHTTPServer.test(HandlerClass = CGIHTTPServer.CGIHTTPRequestHandler,
        ServerClass = BaseHTTPServer.HTTPServer)

# def test(HandlerClass = CGIHTTPRequestHandler,
#          ServerClass = BaseHTTPServer.HTTPServer):
#     SimpleHTTPServer.test(HandlerClass, ServerClass)
# 
# def test(HandlerClass = SimpleHTTPRequestHandler,
#          ServerClass = BaseHTTPServer.HTTPServer):
#     BaseHTTPServer.test(HandlerClass, ServerClass)

def test(HandlerClass = BaseHTTPRequestHandler,
         ServerClass = HTTPServer, protocol="HTTP/1.0"):
    """Test the HTTP request handler class.

    This runs an HTTP server on port 8000 (or the first command line
    argument).

    """

    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = ('', port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)
    # httpd.cgi_directories = ['.',]

    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()
