import RPi.GPIO as gpio
import time

#print(gpio.RPI_INFO)

pin_num=raw_input("Enter pin number where led connected ")

led=int(pin_num)

gpio.setmode(gpio.BOARD)
gpio.setup(led,gpio.OUT,initial=gpio.HIGH)

num=raw_input("Enter no of times ")
freq=raw_input("Enter on/off time ")

for i in range (0,int(num)):
	gpio.output(led,1)
	time.sleep(float(freq))
	print("High now")
	gpio.output(led,0)
	time.sleep(float(freq))
	print("low")

gpio.cleanup()