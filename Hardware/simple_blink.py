import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)
while True:
  gpio.output(4, gpio.HIGH)
  time.sleep(1)
  gpio.output(4, gpio.LOW)
  time.sleep(1)