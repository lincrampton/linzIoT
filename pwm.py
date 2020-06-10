#
# Raspberry PI LED Dimmer using PWM
#
from tkinter import *
import RPi.GPIO as GPIO
from time import sleep

sleepTime = 0.1
pinLED    = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED, GPIO.OUT)

pwm = GPIO.PWM(pinLED, 100)
pwm.start(0)

try:
	while True:                            
		for delta_bright in range(0, 100):
			pwm.ChangeDutyCycle(delta_bright)
			sleep(sleepTime)	
		for delta_dark in range(99, -1, -1):
			pwm.ChangeDutyCycle(delta_dark)
			sleep(sleepTime)	
except KeyboardInterrupt:
	pass

pwm.stop()
GPIO.cleanup()
