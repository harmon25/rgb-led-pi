#!/usr/bin/python

import argparse
from time import sleep
import RPi.GPIO as GPIO

parser = argparse.ArgumentParser(description="Command line program to change the colour of an RGB LED on a Pi")
parser.add_argument('-o','--off', help='turn off led',action='store_true')
parser.add_argument('-v','--verbosity', action="count", default=0,)
on_group = parser.add_argument_group()
on_group.add_argument('-c','--colour', choices=['red', 'green', 'blue', 'yellow', 'cyan', 'purple', 'white'],default='white',help='choose an LED colour')
on_group.add_argument('-b','--blink', help='blinking LED on or off default is off', action='store_true')
on_group.add_argument('-d','--duration', default=10, help='Seconds for the LED to be kept on',type=int)
args = parser.parse_args()

class led_control:
	RGB = [11,13,15] # correspond to pins on the Pi
	GPIO.setmode(GPIO.BOARD)
	def gpio_setup(self):
		RGB = self.RGB
		#GPIO.setmode(GPIO.BOARD)
		for pin in RGB:
			GPIO.setup(pin,GPIO.OUT)
			#GPIO.output(pin,1)
		print "GPIO.setmode(GPIO.BOARD)"
		for pin in RGB:
			print "GPIO.setup({},GPIO.OUT)".format(pin)
			print "GPIO.output({},1)".format(pin)
		
	def colour_check(self,args):
		if args.off == True:
			led_colour = [1,1,1]
		elif args.colour == 'red':
			led_colour = [0,1,1]
		elif args.colour  == 'green':
			led_colour = [1,0,1]
		elif args.colour  == 'blue':
			led_colour = [1,1,0]
		elif args.colour  == 'yellow':
			led_colour = [0,0,1]
		elif args.colour  == 'cyan':
			led_colour = [1,0,0]
		elif args.colour  == 'purple':
			led_colour = [0,1,0]
		elif args.colour  == 'white':
			led_colour = [0,0,0]
		return led_colour


	def led_off(self):
		self.gpio_setup()
		RGB=self.RGB
		GPIO.output(RGB[0],1)
		GPIO.output(RGB[1],1)
		GPIO.output(RGB[2],1)
		print "GPIO.output(RGB[0],1)".format(RGB[0])
		print "GPIO.output(RGB[1],1)".format(RGB[1])
		print "GPIO.output(RGB[2],1)".format(RGB[2])

	def solid(self, args):
		self.gpio_setup()
		RGB=self.RGB
		colour = self.colour_check(args)
		GPIO.output(RGB[0],colour[0])
		GPIO.output(RGB[1],colour[1])
		GPIO.output(RGB[2],colour[2])
		print "RED - GPIO.output({0},{1})".format(RGB[0],colour[0])
		print "GREEN - GPIO.output({0},{1})".format(RGB[1],colour[1])
		print "BLUE - GPIO.output({0},{1})".format(RGB[2],colour[2])
		
	def blink(self,args):
		self.gpio_setup()
		RGB = self.RGB
		time_on = args.duration
		for i in range(0,time_on):
			self.solid(args)
			sleep(1)
			self.led_off()
			sleep(1)
			print "blinking"
		GPIO.cleanup()

	def __init__(self, args):
		time_on = args.duration
		if args.off == True:
			self.led_off()
			GPIO.cleanup()
		if args.blink == True:
			self.blink(args)
		else:
			self.solid(args)
			sleep(time_on)
			GPIO.cleanup()
		

def main():
	print args
	print "Main executing..."
	########################
	led_control(args)
	


if __name__ == '__main__':
		main()
