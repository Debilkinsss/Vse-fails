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

def num2dec(value):
    signal = dec2bin(value)
    gpio.output(dac, signal)
    return signal

try:
    while True:
        for value in range(256):
            time.sleep(0.001)
            signal = num2dec(value)
            voltage = value / levels * maxV
            compV= gpio.input(comp)
            if compV==1:
                print('ADC value = {:^3} -> {}, input volt = {:.2f}'.format(value, signal, voltage))
                break

except KeyboardInterrupt:
    print("\n The program was stopped by the keyboard") 
finally:
    gpio.output(dac, gpio.LOW)
    gpio.cleanup(dac)
