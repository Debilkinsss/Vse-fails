from matplotlib import pyplot
import numpy
from textwrap import wrap
import matplotlib.ticker as ticker

#заполняем список данными из текстового файла
with open('settings.txt') as f:
    settings = [float(i) for i in f.read().split('\n')]

#считываем показания компаратора и переводим через шаг квантования в вольты
data = numpy.loadtxt('data.txt', dtype=int) * settings[1]

#массив времен, создаваемый через количество измерений и известный шаг по времени
data_time=numpy.array([i*settings[0] for i in range(data.size)])
#параметры фигуры
fig, ax = pyplot.subplots(figsize=(16, 10), dpi=500)

#минимальные и максимальные значения для осей
ax.axis([data.min(), data_time.max()+1, data.min(), data.max()+0.2])

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

#название графика с условием для переноса строки и центрированием
ax.set_title("\n".join(wrap('Процесс заряда и разряда конденсатора в RC-цепи', 60)), loc = 'center', fontsize = 17)

#сетка основная и второстепенная
ax.grid(which='major', color = 'k')
ax.minorticks_on()
ax.grid(which='minor', color = 'grey', linestyle = ':')
ax.text(8, 2.1, 'Время заряда: {}c'.format(round(data.argmax()*settings[0], 2)), fontsize=17)
ax.text(8, 1.8, 'Время разряда: {}c'.format(round(data_time.max()-data.argmax()*settings[0], 2)), fontsize=17)

#подпись осей
ax.set_ylabel("Напряжение, В", fontsize = 17)
ax.set_xlabel("Время, с", fontsize = 17)

#линия с легендой
ax.plot(data_time, data, c='blue', linewidth=1.5, label = 'V(t)')
ax.scatter(data_time[0:data.size:20], data[0:data.size:20], marker = 'o', c = 'red', s=35)

ax.legend(shadow = False, loc = 'right', fontsize = 20)


#сохранение
fig.savefig('graph1.png')
#fig.savefig('graph.svg')


