import socket
import threading
from HttpResponse import HttpResponse, HttpResponseStatus


# Define class for threading
class HandleRequestThread(threading.Thread):
    def __init__(self, jelly_web_server, client_socket, address):
        threading.Thread.__init__(self)
        if isinstance(jelly_web_server, JellyWebServer):
            self.server = jelly_web_server
            self.client_socket = client_socket
            self.address = address
        else:
            raise TypeError("Expected first argument to be of type JellyWebServer")

    def run(self):
        request = self.client_socket.recv(1000)
        print("From: "+str(self.address) + "\n" + request.decode())
        self.server.send_response(self.client_socket)


class JellyWebServer:

    def __init__(self, address):
        self.address = address
        self.running = False

    def send_response(self, client_socket):
        if self.running:
            response = HttpResponse(HttpResponseStatus(200))
            body = "<!DOCTYPE html><html><body>It works!</body></html>"
            content_type = "text/html; charset=utf-8"
            response.set_body(body, content_type)
            response.build()
            # sending response
            client_socket.send(bytes(str(response).encode()))
        else:
            raise Exception("Server is off, start the server first")

    def start_server(self):
        s = None
        try:
            # create an I_NET, STREAMing socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print("Creating socket: " + str(s))
            # bind the socket to public host,
            # and a well-known port
            port = 80
            address = 'localhost'
            print("Creating socket for address: " + str(address))
            s.bind((address, port))
            # become a server socket
            s.listen(5)
            print("Listening to port: " + str(port))
            self.running = True

            while True:
                # accept connections from outside
                (client_socket, address) = s.accept()
                print("New Client Connected: "+str(address)+')')
                # pass client to thread
                thread = HandleRequestThread(self, client_socket, address)
                thread.start()
        finally:
            s.close()


server = JellyWebServer("localhost")
server.start_server()


