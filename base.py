import RPi.GPIO as gpio
import time

print(gpio.RPI_INFO)

gpio.setmode(gpio.BOARD)
gpio.setup(4,gpio.OUT,initial=gpio.HIGH)
time.sleep(1)
print("High now")
gpio.output(4,0)
time.sleep(1)
print("low")