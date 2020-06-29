import time
import os
from pyBases import *


class Logger:
    def __init__(self,scriptName,enableDebug = False):
        self.scriptName = scriptName
        self.enableDebug = enableDebug

    def setDebugMode(self,debugMode):
        self.debugMode = debugMode

    def info(self,data):
        self.printWithoutReturn("[INFO]  ",color=color_purple)
        self.printWithoutReturn(self.scriptName+" ")
        self.printWithoutReturn(str(time.time())+" : ",color=color_green)
        self.printWithoutReturn(str(os.getpid()),color=color_purple)
        self.printWithoutReturn(" : ")
        print(str(data))
        # self.printWithoutReturn("\033[35m[INFO]  ")
        # self.printWithoutReturn("\033[0m"+self.scriptName+" ")
        # self.printWithoutReturn("\033[32m"+str(time.time()))
        # self.printWithoutReturn(" : ")
        # print(str(data))


    def debug(self,data):
        if self.enableDebug:
            self.printWithoutReturn("[DEBUG] ")
            self.printWithoutReturn(self.scriptName + " ")
            self.printWithoutReturn(str(time.time()) + " : ", color=color_green)
            self.printWithoutReturn(str(os.getpid()), color=color_purple)
            self.printWithoutReturn(" : ")
            print(str(data))

    def warn(self,data):
        #print("[WARN]  " + self.scriptName + " " + str(time.time()) + " : " + str(data))
        self.printLogLine("WARN ",data)

    def error(self,data,e = Null):
        self.printLogLine("ERROR",data)
        if not e == Null:
            self.error(str(e))

    def printWithoutReturn(self,data,color=color_default):
        betterPrint(data,enter=false,color=color)

    def printLogLine(self,level,data):
        def printData(data,level,color):
            self.printWithoutReturn("["+level+"] ",color=color)
            self.printWithoutReturn(self.scriptName+" ")
            self.printWithoutReturn(str(time.time())+" ",color=color_green)
            self.printWithoutReturn(str(os.getpid()),color=color_purple)
            self.printWithoutReturn(" : ")
            print(str(data))

        if level == "INFO":
            printData(data,level,color_purple)
        elif level == "DEBUG":
            printData(data,level,color_default)
        elif level == "WARN ":
            printData(data,level,color_yellow)
        elif level == "ERROR":
            printData(data,level,color_red)
