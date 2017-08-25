import RPi.GPIO as gpio
import time

print(gpio.RPI_INFO)

gpio.setmode(gpio.BOARD)
gpio.setup(7,gpio.OUT,initial=gpio.HIGH)

num=raw_input("Enter no of times ")
freq=raw_input("Enter on/off time ")

for i in range (0,int(num)):
	gpio.output(7,1)
	time.sleep(float(freq))
	print("High now")
	gpio.output(7,0)
	time.sleep(float(freq))
	print("low")

gpio.cleanup()