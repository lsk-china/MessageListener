import RPi.GPIO as GPIO
from pyBases import *
from pyLog import Logger

logger = Logger("hardware",true)
inited = false

GPIO0 = 11
GPIO1 = 10
GPIO2 = 13
GPIO3 = 15
GPIO4 = 16
GPIO5 = 18
GPIO6 = 22
GPIO7 = 7
GPIO21 = 29
GPIO22 = 31
GPIO23 = 33
GPIO24 = 35
GPIO25 = 37
GPIO26 = 32
GPIO27 = 36
GPIO28 = 38
GPIO29 = 40

OUTPUT = GPIO.OUT
INPUT = GPIO.IN

HIGH = 1
LOW = 0

def hardwareInit():
	logger.info("Start setup hardware.")
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(false)
	logger.info("Setup done!")

def pinMode(pin,mode):
	GPIO.setup(pin,mode)
	logger.info("pin "+str(pin)+" mode "+str(mode))

def digitalWrite(pin,state):
	GPIO.output(pin,state)
	logger.info("pin "+str(pin)+" state "+str(state))

def hardwareCleanup():
	GPIO.cleanup()
	logger.info("Hardware cleanup done!")

