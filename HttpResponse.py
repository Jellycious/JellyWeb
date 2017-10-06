from HttpResponseStatus import HttpResponseStatus


class HttpResponse:

    def __init__(self, response_type):
        if isinstance(response_type, HttpResponseStatus):
            self.response_type = response_type
            self.connection_line = "Connection: keep-alive\n"
        else:
            raise TypeError("response_type must be of type HttpResponseStatus")

    def close_connection(self):
        self.connection_line = "Connection: close\n"

    def __str__(self):
        status_line = "HTTP/1.1 "+str(self.response_type.value)+" "+str(self.response_type)+"\n"
        return status_line


# Testing Purposes Only
r = HttpResponse(HttpResponseStatus(200))
print(str(r))
