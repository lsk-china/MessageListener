import time
from hardware import *
from pyBases import *
from pyLog import Logger
from api import messageCount,apiInit
#from pyPropertise import *
from client import send
import sys
from configs import *

#propertiesFile = parse("")
logger = null
delay = 0

def init():
	global logger,delay
	logger = Logger("MessageListener",false)
	logger.info("Begin global initalizition.")
	initConfig()
	debugMode = getDebugMode()
	delay = getRefreshRate()
	logger.setDebugMode(debugMode)
	hardwareInit()
	ledInit()
	ledClear()
	apiInit(debugMode)
	logger.info("Global initalizition done!")

def ledInit():
	pinMode(GPIO2,OUTPUT)
	pinMode(GPIO3,OUTPUT)
	pinMode(GPIO4,OUTPUT)

def ledClear():
	digitalWrite(GPIO2,HIGH)
	digitalWrite(GPIO3,HIGH)
	digitalWrite(GPIO4,HIGH)

def onLike(num):
	digitalWrite(GPIO3,LOW)

def onComment(num):
	digitalWrite(GPIO2,LOW)

def onSystem(num):
        digitalWrite(GPIO4,LOW)

def check():
	global delay
	delay = getRefreshRate()
	comment,like,system = messageCount()
	if not comment == 0:
		onComment(comment)
	if not like == 0:
		onLike(like)
	if not system == 0:
		onSystem(system)
	if comment == 0 and like == 0 and system == 0:
		ledClear()
	else:
		send(comment,like,system)
	time.sleep(delay)

def stop():
	logger.info("Begin global cleanup.")
	hardwareCleanup()
	stopConfig()
	logger.info("Evering is clean.")

def main():
	#GPIO.setmode(GPIO.BOARD)
	#initLED()
	#clearLED()
	#try:
	#	while True:
	#		refresh()
	#		if haveMessage():
	#			if comment != 0:
	#				commentLED()
	#			if like != 0:
        #                                likeLED()
	#			if system != 0:
        #                               systemLED()
	#		else:
	#			clearLED()
	#		time.sleep(10)
	#except:
	#	GPIO.cleanup()
	#enableDebug = parseBoolean(sys.argv[1]) == null ? false : parseBoolean(sys.argv[1])
	init()
	try:
		while true:
			check()
	except:
		stop()

if __name__ == "__main__":
	main()


