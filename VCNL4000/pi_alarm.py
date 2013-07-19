#!/usr/bin/python

from VCNL4000 import VCNL4000
import time
import RPi.GPIO as GPIO
import os

# Initialise the VNCL4000 sensor
vcnl = VCNL4000(0x13)

# Initialize GPIO for the LED
gpio_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin,GPIO.OUT)
GPIO.output(gpio_pin,False)

# Print proximity sensor data every 100 ms
while True:
	
	# Get data from the sensor
	proximity = vcnl.read_proximity()
	
	# If the threshold is crossed, start the alarm
	if (proximity > 3000):
		GPIO.output(gpio_pin,True)
		os.system("aplay alarm_sound.wav")
		GPIO.output(gpio_pin,False)
		
	time.sleep(0.1)
