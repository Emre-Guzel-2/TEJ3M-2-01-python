#Emre Guzel
# Feb 11 2026

import board
import digitalio
import time

#settign the led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(.5)
    led.value = False
    time.sleep(1)




