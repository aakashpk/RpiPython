import RPi.GPIO as gpio
import time

print(gpio.RPI_INFO)

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT,initial=gpio.HIGH)

a=raw_input("Enter no of times")

while(1):
	gpio.output(7,1)
	time.sleep(1)
	print("High now")
	gpio.output(7,0)
	time.sleep(1)
	print("low")

gpio.cleanup()