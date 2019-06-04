################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
from http.server import BaseHTTPRequestHandler, HTTPServer
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
servo1= GPIO.PWM(13, 100)
QueryString = None
x = None
list2 = None
i = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global QueryString, x, list2, i
    messagetosend = bytes('Getting Query String',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    QueryString = self.requestline
    QueryString = QueryString[5 : int(len(QueryString)-9)]
    print('Sting Prior to Loop')
    print(QueryString)
    print('Loop through list')
    x = QueryString
    list2 = x.split(',')
    for i in range(1, 6):
      print(i)
      print(list2[int(i - 1)])
      servo1.start(10)
      dutyCycle = ((float((list2[int(i - 1)])) * 0.01) + 0.5) * 10
      servo1.ChangeDutyCycle(dutyCycle)
      GPIO.cleanup()
    return


server_address_httpd = ('192.168.86.54',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Server Started')
httpd.serve_forever()
