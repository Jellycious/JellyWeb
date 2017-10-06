import socket
import threading


# Define class for threading
class HandleRequestThread(threading.Thread):
    def __init__(self, client_socket, address):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.address = address

    def run(self):
        request = self.client_socket.recv(1000)
        print("From: "+str(self.address) + "\n" + request.decode())
        send_response(self.client_socket)


def send_response(client_socket):
    response_body = "<html><body>It Works!</body></html>"
    response_version = "HTTP-Version: HTTP/1.1 200 OK\n"
    response_server = "Server: JellyWebserver \n"
    response_allow_control = "Access-Control-Allow-Origin: *\n"
    response_content_length = get_content_length_header(response_body)
    response_content_type = "Content-Type: text/html; charset=utf-8\n"
    response = response_version + response_server + response_allow_control + response_content_length + response_content_type + "\n" + response_body
    # sending response
    client_socket.send(bytes(response.encode()))


def get_content_length_header(body):
    length = len(body)
    header = "Content-Length: " + str(length) + "\n"
    return header


def start_server():
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

        while True:
            # accept connections from outside
            (client_socket, address) = s.accept()
            print("New Client Connected: "+str(address)+')')
            # pass client to thread
            thread = HandleRequestThread(client_socket, address)
            thread.start()
    finally:
        s.close()


# start the actual server
start_server()
