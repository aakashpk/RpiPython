import RPi.GPIO as gpio
import time

print(gpio.RPI_INFO)

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT,initial=gpio.HIGH)

gpio.output(7,1)
gpio.output(7,0)
// Another check
gpio.cleanup()