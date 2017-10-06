import sys
import socket
import threading
import serverlogger
'''
WebServer providing rest functionality for getting book quotes and etc...
'''

#Define class for threading
class handleRequestThread(threading.Thread):
	def __init__(self, clientsocket, address):
		threading.Thread.__init__(self)
		self.clientsocket = clientsocket
		self.address = address

	def run(self):
		request = self.clientsocket.recv(1000)
		sendResponse(self.clientsocket)

def sendResponse(clientsocket):
	responseBody = "<html><body>It Works!</body></html>"
	responseVersion = 	"HTTP-Version: HTTP/1.0 200 OK\n"
	responseServer = "Server: JellyWebserver \n"
	responseAllowControl = "Access-Control-Allow-Origin: *\n"
	responseContentLength = getContentLengthHeader(responseBody)
	responseContentType = "Content-Type: text/html; charset=utf-8\n"
	response = responseVersion + responseServer + responseAllowControl + responseContentLength + responseContentType +"\n"+ responseBody
	#sending response
	clientsocket.send(bytes(response.encode()))	

def getContentLengthHeader(body):
	length = len(body)
	header = "Content-Length: "+str(length)+"\n"
	return header

def startServer ():
	try:

		#create an INET, STREAMing socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		print("Creating socket: "+str(s))
		#bind the socket to public host,
		#and a well-known port
		port = 80
		address = '192.168.2.42'
		print("Creating socket for address: "+str(address))
		s.bind((address, port))
		#become a server socket
		s.listen(5)
		#start beercounter
		bc.startCounting()
		print("Listening to port: " + str(port))

		while True:

			#accept connections from outside
			(clientsocket, address) = s.accept()
			print("New Client Connected: str(address)")
			serverlogger.log("New Connection: "+str(address))
			#pass client to thread
			thread = handleRequestThread(clientsocket, address)
			thread.start()
	finally:
		s.close()

#start the actual server
startServer()
