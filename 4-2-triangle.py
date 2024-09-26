import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


try:
    T = input('Period is: ')
    while(True):
        for i in range(256):
            GPIO.output(dac, dec2bin(i))
            print(3.3 * i / 256)
            time.sleep(float(T)/512)
        
        for j in range(255, 0, -1):
            GPIO.output(dac, dec2bin(j))
            print(3.3*j/256)
            time.sleep(float(T)/512)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()