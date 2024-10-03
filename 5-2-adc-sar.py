import RPi.GPIO as gpio
import time
gpio.setwarnings(False)

gpio.setmode(gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
bits = 8
levels = 2**8
maxV =3.3
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(bits)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, dec2bin(k))
        time.sleep(0.01)
        if gpio.input(comp)==1:
            k-=2**i
    return k

try:
    while True:
        n = adc()
        if n!=0 and n:
            print('ADC value=', n, 'input value=', "{:.2f}".format(3.3*n/256))

except KeyboardInterrupt:
    print("\n The program was stopped by the keyboard") 
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
