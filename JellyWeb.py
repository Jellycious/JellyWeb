import socket
import threading
from HttpResponse import HttpResponse, HttpResponseStatus
from HttpRequest import HttpRequest
from resource_getter import get_file
import StandardizedResponses


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
        request_bytes = self.client_socket.recv(4096)
        try:
            request = HttpRequest(request_bytes)
            print("URI='"+request.get_uri()+"'")
            response = self.handle_request(request)
            response.build()
            self.server.send_response(self.client_socket, response)
        except Exception as e:
            print(e)
            self.server.send_response(self.client_socket, StandardizedResponses.get_internal_server_error())

    def handle_request(self, request):
        request_method = request.get_method()
        if request_method == 'GET':
            return self.handle_get_request(request)
        else:
            return HttpResponse(HttpResponseStatus(501))

    def handle_get_request(self, get_request):
        if get_request.get_method() == 'GET':
            uri = get_request.get_uri()
            if uri == "/":
                body = get_file("index.html")
                content_type = "text/html; charset=utf-8"
                response = HttpResponse(HttpResponseStatus(200))
                response.set_body(body, content_type)
                return response
            else:
                try:
                    body = get_file(uri)
                    response = HttpResponse(HttpResponseStatus(200))
                    response.set_body(body, "image/x-icon")
                    return response
                except Exception as e:
                    if isinstance(e, FileNotFoundError):
                        return HttpResponse(HttpResponseStatus(404))
                    else:
                        pass
        else:
            raise Exception("Method not of type GET")


class JellyWebServer:

    def __init__(self, address):
        self.address = address
        self.running = False
        self.clients = []

    def send_response(self, client_socket, response):
        if self.running:
            # sending response
            print("sending response: "+str(response))
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
                self.clients.append((client_socket, address))
                print("New Client Connected: "+str(address)+')')
                # pass client to thread
                thread = HandleRequestThread(self, client_socket, address)
                thread.start()
        finally:
            s.close()


server = JellyWebServer("localhost")
server.start_server()


