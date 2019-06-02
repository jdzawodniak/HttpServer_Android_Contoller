################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
from http.server import BaseHTTPRequestHandler, HTTPServer

QueryString = None
x = None
y = None
list2 = None
i = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global QueryString, x, y, list2, i
    messagetosend = bytes('Getting Query String',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    QueryString = self.requestline
    QueryString = QueryString[5 : int(len(QueryString)-9)]
    print(QueryString)
    print('Loop through list')
    x = QueryString
    y = x.split(',')
    list2 = x.split(',')
    for i in range(1, 6):
      print(i)
      print(list2[int(i - 1)])
    return


server_address_httpd = ('192.168.86.54',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Server Started')
httpd.serve_forever()
