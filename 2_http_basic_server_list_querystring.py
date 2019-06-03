################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
from http.server import BaseHTTPRequestHandler, HTTPServer

QueryString = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global QueryString
    QueryString = self.requestline
    QueryString = QueryString[5 : int(len(QueryString) - 9)]
    print('You got a request')
    print(QueryString)
    messagetosend = bytes(QueryString,"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    return


server_address_httpd = ('192.168.86.54',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting Server')
httpd.serve_forever()
