# RPi.GPIO event detection
# Import the required module. 
import RPi.GPIO as GPIO 
import time
def do_stuff(channel):
	print 'Hey you pressed a button!!' 
# Set the mode of numbering the pins. 
GPIO.setmode(GPIO.BCM) 
# GPIO pin 10 is the output. 
GPIO.setup(10, GPIO.OUT) 
# GPIO pin 8 is the input. 
GPIO.setup(8, GPIO.IN) 
# Initialise GPIO10 to high (true) so that the LED is off. 
GPIO.output(10, True) 
# Add a event detector to the input pin. It will check when the input is high
GPIO.add_event_detect(8,GPIO.FALLING)

# What about if you want to do just a function callback?
GPIO.add_event_callback(8, callback = do_stuff, bouncetime=200)
while 1:
	if GPIO.event_detected(8):
		print 'Button Pressed'
	time.sleep(.01)





