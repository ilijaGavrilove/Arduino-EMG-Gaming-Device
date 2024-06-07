from serial import Serial
from time import sleep
from pyautogui import keyUp, keyDown
from config import PORT, MY_MTF

ser = Serial(PORT, 9600)

try:
    print('Значения из порта', ser.port)
    while True:
        emgValue = ser.readline().decode().strip()
        sleep(0.1)
        if int(emgValue) >= MY_MTF:
            keyDown(' ')
            sleep(0.05)
            keyUp(' ')
        print(emgValue)

except KeyboardInterrupt:
    print('Программа остановлена')
    ser.close()
