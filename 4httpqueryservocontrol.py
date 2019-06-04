################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import RPi.GPIO as GPIO
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
servo1= GPIO.PWM(13, 100)
QueryString = None
x = None
list2 = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global QueryString, x, list2
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
    servo1.start(10)
    print(list2[int((int('1')) - 1)])
    dutyCycle = ((float((int((list2[int((int('1')) - 1)])))) * 0.01) + 0.5) * 10
    servo1.ChangeDutyCycle(dutyCycle)
    time.sleep(3)
    print(list2[int((int('2')) - 1)])
    dutyCycle = ((float((int((list2[int((int('2')) - 1)])))) * 0.01) + 0.5) * 10
    servo1.ChangeDutyCycle(dutyCycle)
    time.sleep(3)
    print(list2[int((int('3')) - 1)])
    dutyCycle = ((float((int((list2[int((int('2')) - 1)])))) * 0.01) + 0.5) * 10
    servo1.ChangeDutyCycle(dutyCycle)
    time.sleep(3)
    dutyCycle = ((float((int((int('0'))))) * 0.01) + 0.5) * 10
    servo1.ChangeDutyCycle(dutyCycle)
    print('0')
    GPIO.cleanup()
    return


server_address_httpd = ('192.168.86.54',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Server Started')
httpd.serve_forever()
