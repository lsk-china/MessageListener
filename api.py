from pyLog import Logger
from pyBases import *
import requests
from requests.cookies import RequestsCookieJar
from json import dumps,loads
from bs4 import BeautifulSoup

logger = null
def apiInit(enableDebug):
	global logger
	logger = Logger("api",enableDebug)

cache = {
	"authorization" : ""
}

class Response:
	def __init__(self,text,cookies):
		self.text = text
		self.cookies = cookies

	def getCookie(self,key):
		return self.cookies[key]

	def getText(self):
		return self.text

	def cookieDict(self):
		return self.cookies


def login():
	ses = requests.session()
	headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
	shequ = requests.get('https://shequ.codemao.cn', headers = headers)
	soup = BeautifulSoup(shequ.text, 'html.parser')
	pid = loads(soup.find_all("script")[0].string.split("=")[1])['pid']
	logger.debug("pid : "+str(pid))
	a = ses.post('https://api.codemao.cn/tiger/v3/web/accounts/login', headers = headers,data = dumps({"identity": "edu1011598019", "password": "lsk123456", "pid": pid}))
	cookies = a.cookies.get_dict()
	logger.debug(cookies)
	logger.info("authorization : "+cookies["authorization"])
	loginResp = Response(a.text,cookies)
	shequResp = Response(shequ.text,shequ.cookies.get_dict())
	return loginResp,shequResp

def privateMessageCount(authorization):
	cookie_jar = RequestsCookieJar()
	cookie_jar.set("authorization",authorization)
	resp = requests.get("https://api.codemao.cn/web/message-record/count",cookies = cookie_jar)
	respJson = resp.json()
	commentJson = respJson[0]
	comment = commentJson["count"]
	likeJson = respJson[1]
	like = likeJson["count"]
	systemJson = respJson[2]
	system = systemJson["count"]
	logger.info("comment : "+str(comment))
	logger.info("like : "+str(like))
	logger.info("system : "+str(system))
	return comment,like,system

def messageCount():
	if cache["authorization"] == "":
		loginResp,shequResp = login()
		cache["authorization"] = loginResp.getCookie("authorization")
	else:
		logger.info("Using cached authorization data : "+cache["authorization"])
	try:
		logger.info("Getting message count......")
		return privateMessageCount(cache["authorization"])
	except Exception as e:
		logger.error("Get message count failed. Retrying...",e=e)
		cache["authorization"] = ""
		return messageCount()

