import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
led = [2, 3, 4, 17, 27, 22, 10, 9]
gpio.setup(led, gpio.OUT, initial = 1)
pwm = gpio.PWM(2, 1000)
pwm.start(0)

try:
    while(True):
        k = int(input())
        pwm.ChangeDutyCycle(k)
        print("{:.2f}".format(k*3.3/100))
finally:
    gpio.cleanup()
