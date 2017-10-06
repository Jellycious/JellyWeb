import time

path_to_workspace = "/home/pi/Development/BookQuoteAPI/server/workspace/" 
def logMessage(msg):
	logFile = open(path_to_workspace+"server.log", "a+")
	logFile.write(getTimeStamp()+msg+"\n")
	logFile.close();

def log(address):
	text = "New Connection From: "+str(address)
	logMessage(text)


def getTimeStamp():
	return time.strftime("[%d-%m-%Y %H:%M:%S]")
