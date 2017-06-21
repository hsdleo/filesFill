import RPi.GPIO as GPIO
import time
from time import sleep
# Pin Definitons:
sensorPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Button pin set as input w/ pull-up

# Initial state for LEDs:

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(sensorPin): # button is released
            print("Detectou sensor")
        else: # button is pressed:
            print("Saiu sensor")
	sleep(0.1)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
