# Import the required module. 
import RPi.GPIO as GPIO 
import time
# Set the mode of numbering the pins. 
GPIO.setmode(GPIO.BCM) 
# GPIO pin 10 is the output. 
GPIO.setup(10, GPIO.OUT) 
# GPIO pin 8 is the input. 
GPIO.setup(24, GPIO.IN) 
# Initialise GPIO10 to high (true) so that the LED is off. 
GPIO.output(10, True) 
while 1: 
    if GPIO.input(24): 
        GPIO.output( 10, False)
	print "hre" 
    else: 
        # When the button switch is not pressed, turn off the LED. 
        GPIO.output( 10, True)
	print('hel')
    time.sleep(1)
