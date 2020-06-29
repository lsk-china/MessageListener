from pyBases import *
from pyLog import Logger
import socket

logger = Logger("client",true)
address = ("192.168.31.113",11000)

def send(comment,like,system):
	data = str(comment) + "," + str(like) + "," + str(system)
	logger.info("Sending data : "+data)
	try:
		s = socket.socket()
		s.connect(address)
		s.send(data.encode())
		s.close()
	except Exception as e:
		logger.error("Send failed!",e=e)
	else:
		logger.info("Send success!")

