''' The SOS Python Script
    Created by Micah Hoffman, Jan 2018
    
    Purpose: Turn on and off an LED using python and
             make it blink S-O-S in Morse code
'''           

# What pin on the Pi should be used to send the signals?
out_pin = 4


# Load functions
import RPi.GPIO as GPIO
import time

# Set up some of the settings we need to control the pin
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(out_pin,GPIO.OUT)

print('Now sending the "S" character (dot dot dot)')
# Start a FOR loop and do what is inside it 3 times
for var1 in range(0,3):
    # Send a "HIGH OUPUT" to the pin you specified above.
    # This sends the current the LED needs to turn on.
    GPIO.output(out_pin,GPIO.HIGH)
    # The sleep command just pauses the script to allow the
    # LED to stay on for a certain amount of time.
    time.sleep(.25)
    # Now we change the output to the pin to make the LED turn off
    GPIO.output(out_pin,GPIO.LOW)
    # Wait a certain amount of time (sleep)
    time.sleep(.5)

# We are not commenting the code below because it does the same thing
# as above, just with different pause (sleep) values

print('Now sending the "O" character (dash dash dash)')
for var1 in range(0,3):
    GPIO.output(out_pin,GPIO.HIGH)
    time.sleep(.75)
    GPIO.output(out_pin,GPIO.LOW)
    time.sleep(.5)
    
print('Now sending the "S" character (dot dot dot)')
for var1 in range(0,3):
    GPIO.output(out_pin,GPIO.HIGH)
    time.sleep(.25)
    GPIO.output(out_pin,GPIO.LOW)
    time.sleep(.5)

# Turn off the LED
GPIO.setup(out_pin,GPIO.OUT)