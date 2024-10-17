import RPi.GPIO as gpio
import time
from matplotlib.pyplot import pyplot

gpio.setmode(gpio.BCM)
#nastraivaem GPIO na Raspberry Pi

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

gpio.setup(dac, gpio.OUT, initial = gpio.HIGH)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

print("амам")
def dec2bin(dec):
    return [int(bit) for bit in bin(dec)[2:].zfill(bits)]

#reading from troyka
def adc():
    k = 0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, dec2bin(k))
        time.sleep(0.005)
        if gpio.input(comp)==0: # last time there was 1
            k-=2**i
    return k

try:
    napr = 0
    result_ismer = []
    time_start = time.time()
    count = 0
    #condensator na zaryadke, zapisivaem ego pokazania in process
    print("Start zaryada")
    while napr<256*0.25: #maybe 0.97
        print("Idet zaryadka...")
        napr = adc()
        result_ismer.append(napr)
        #time.sleep(0)
        count+=1
        gpio.output(leds, dec2bin(napr))
    gpio.setup(troyka, gpio.OUT, initial = gpio.LOW)
    #rasryadka condensatora, zapis pokazania in process
    print("Srart razryada")
    while napr>256*0.02:
        print("Idet razryadka...")
        napr = adc()
        result_ismer.append(napr)
        #time.sleep(0)
        count+=1
        gpio.output(leds, dec2bin(napr))
    time_exp = time.time() - time_start
    #zapis dannix v fail
    with open('data.txt', 'w') as f:
        for i in result_ismer:
            f.write(str(i)+'\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_exp/count) + '\n')
        f.write(str(3.3/2**(8-1)))
        f.write('0.01289')
    print('Prodolgitelnost experimenta {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_exp, time_exp/count, 1/time_exp/count, 0.013))
    #graficsss
    print('Postroenie graficov')
    y = [i/256*3.3 for i in result_ismer]
    x = [i*time_exp/count for i in range(len(result_ismer))]
    pyplot.plot(x, y)
    pyplot.xlabel('Time')
    pyplot.ylabel('Voltage')
    pyplot.show()

finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.output(leds, 0)
    gpio.cleanup()