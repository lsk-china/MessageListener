from pyBases import *
from pyLog import Logger
from pyProperties import *
from multiprocessing import Process,Value
import socket

properties = null
debugMode = false
port = 11000
host = "0.0.0.0"
logger = null
serverProcess = null
refreshRate = Value("f",10.0)

def initConfig():
	global properties,debugMode,port,serverProcess,logger
	logger = Logger("configs",true)
	logger.info("Loading properties-file......")
	try:
		properties = parse("MessageListener.properties")
		debugMode = parseBoolean(properties.get("messagelistener.core.debug"))
		refreshRate.value = float(properties.get("messagelistener.core.refresh-rate"))
		port = int(properties.get("messagelistener.server.port"))
		host = properties.get("messagelistener.server.host")
		logger.info("Done!")
		logger.info("Starting config server......")
		p = ServerProcess(host,port,refreshRate)
		p.start()
		serverProcess = p
	except Exception as e:
		logger.error("Configs model initalzition failed!",e=e)

#def serverProcess():
#	global refreshRate
#	serverSocket = socket.socket()
#	serverSocket.bind((host,port))
#	serverSocket.listen(5)
#	logger.info("Done!")
#	logger.info("Configs model initalzition done!")
#	while true:
#		try:
#			conn,addr = serverSocket.accept()
#			data = conn.recv(1024).decode()
#			logger.info(data)
#			datas = data.split(",")
#			refershRate = int(datas[0])
#			conn.close()
#		except Exception as e:
#			logger.error("Failed to processing request.",e=e)

class ServerProcess(Process):
	def __init__(self,host,port,refreshRate):
		Process.__init__(self)
		logger = Logger("ServerProcess",true)
		logger.info("Initalzing server")
		serverSocket = socket.socket()
		serverSocket.bind((host,port))
		serverSocket.listen(5)
		logger.info("Initalzition server done!")
		self.serverSocket = serverSocket
		self.logger = logger
		self.refreshRate = refreshRate

	def run(self):
		logger = self.logger
		while true:
			try:
				conn,addr = self.serverSocket.accept()
				data = conn.recv(1024).decode()
				logger.info(data)
				datas = data.split(",")
				self.refreshRate.value = float(datas[0])
				logger.debug(self.refreshRate.value)
				#self.setRefreshRate(refreshRate)
			except Exception as e:
	                       logger.error("Failed to processing request.",e=e)
			finally:
				conn.close()
	def terminate(self):
		Process.terminate(self)
		self.serverSocket.close()

def getRefreshRate():
	return refreshRate.value

def getDebugMode():
	return debugMode

def setRefreshRate(tarRefreshRate):
	refreshRate.value = tarRefreshRate

def stopConfig():
	logger.info("Stopping config server......")
	serverProcess.terminate()
	logger.info("Done!")
