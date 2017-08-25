import RPi.GPIO as gpio
import time

#pin assignment, port number in bracket
led1=int(11) 
led2=int(7)

port_initialize():
	gpio.setmode(gpio.BOARD)
	gpio.setup(led1,gpio.OUT)

port_initialize()

gpio.output(led,1)
gpio.output(led,0)

gpio.cleanup()