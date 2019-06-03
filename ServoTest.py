################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
servo1= GPIO.PWM(13, 100)


servo1.start(10)
for count in range(10):
  dutyCycle = ((float(0) * 0.01) + 0.5) * 10
  servo1.ChangeDutyCycle(dutyCycle)
  time.sleep(2)
  dutyCycle = ((float(90) * 0.01) + 0.5) * 10
  servo1.ChangeDutyCycle(dutyCycle)
  time.sleep(2)
  dutyCycle = ((float(180) * 0.01) + 0.5) * 10
  servo1.ChangeDutyCycle(dutyCycle)
  time.sleep(2)
GPIO.cleanup()
