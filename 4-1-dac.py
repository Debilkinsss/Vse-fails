import RPi.GPIO as GPIO
import sys

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    while(True):
        a = input('input 0-255: ')
        if a=='q':
            sys.exit()
        elif ((int(a)>-1) and (int(a)<256)) and a.isdigit() and int(a)%1==0:
            GPIO.output(dac, decimal2binary(int(a)))
            print("{:.4f}".format(int(a)/256*3.3), 'V')
        elif not a.isdigit():
            print('input numbers from 0 to 255')



except ValueError:
    print('input number from 0 to 255!')
except KeyboardInterrupt:
    print('done!')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()