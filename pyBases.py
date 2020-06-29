Null = None
null = None
true = True
false = False

color_default = "\033[0m"
color_purple = "\033[35m"
color_green = "\033[32m"
color_red = "\033[31m"
color_yellow = "\033[33m"

def betterPrint(data, end="", enter=true, color=color_default):
    printData = color+data+end
    if enter:
        print(printData)
    else:
        print(printData,end="")

def default():
	pass

def switch(data,cases,handlers,handleDefault=default,isBreak=true):
    executed = false
    if not (len(cases) == len(handlers)) :
        return
    for i in range(0,len(cases)):
        if(str(data) == cases[i]):
            handler = handlers[i]
            handler()
            executed = true
            if isBreak:
                return
    if not executed:
        handlDefault()

def parseBoolean(string):
    if string == "true" or string == "True":
        return true
    elif string == "false" or string == "False":
        return false
    else:
        return null
