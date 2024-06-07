from serial import Serial
import matplotlib.pyplot as plt
from time import sleep

ser = Serial('COM4', 9600)

plt.ion()  # Включаем интерактивный режим

fig, ax = plt.subplots()
valuesCount = 0
x = []
y = []

# Цикл для добавления данных
while True:
    emgValue = ser.readline().decode().strip()
    x.append(valuesCount)
    y.append(int(emgValue))

    ax.plot(x, y, 'r-')  # Рисуем график
    ax.set_xlabel('Количество итераций')
    ax.set_ylabel('Значение ЭМГ')
    ax.set_title('ЭМГ')
    fig.canvas.draw()  # Обновляем график
    fig.canvas.flush_events()  # Очищаем очередь событий
    valuesCount += 1
    sleep(0.1)

plt.ioff()  # Выключаем интерактивный режим
plt.show()  # Покажем график

