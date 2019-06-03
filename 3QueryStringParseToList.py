################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
from http.server import BaseHTTPRequestHandler, HTTPServer

QueryString = None
querystringlist = None
i = None
list2 = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global QueryString, querystringlist, i, list2
    QueryString = self.requestline
    QueryString = QueryString[5 : int(len(QueryString) - 9)]
    print(QueryString)
    querystringlist = QueryString.split(',')
    for i in range(1, 7):
      print(i)
      print(list2[int(i - 1)])
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
