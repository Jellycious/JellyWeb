from enum import Enum
from datetime import datetime


class HttpResponse:

    http_response_order = ['status', 'date', 'connection', 'server', 'access-control-allow-origin', 'accept-ranges',
                           'content-type', 'content-length', 'last-modified', 'body']

    def __init__(self, response_type, connection_alive=False):
        if isinstance(response_type, HttpResponseStatus):
            self.response_type = response_type
            self.connection_alive = connection_alive
            self.version = "HTTP/1.1"
            self.server = "JellyWeb"
            self.allow_origin = "*"

            self.headers = {}
            self.is_build = False
            self.body = None
            self.content_type = None
            self.content_length = None
            self.last_modified = None
            self.accept_ranges = None

        else:
            raise TypeError("response_type must be of type HttpResponseStatus")

    def set_accept_ranges(self, accept_ranges):
        self.accept_ranges = accept_ranges

    def set_body(self, body, content_type="text/plain"):
        if len(body) == 0:
            raise Exception("body cannot have length 0")
        self.body = body
        self.content_type = content_type
        self.content_length = len(body)

    def get_body(self):
        return self.body

    def get_body_info(self):
        return self.content_type, self.content_length

    def get_accept_ranges(self):
        return self.accept_ranges

    def set_keep_alive(self, keep_alive):
        self.connection_alive = keep_alive

    def get_keep_alive(self):
        return self.connection_alive

    def set_response_type(self, response_type):
        self.response_type = response_type

    def get_response_type(self):
        return self.response_type

    def build(self):
        self.headers['status'] = self.version+" "+str(self.response_type.value)+" "+str(self.response_type)
        self.headers['date'] = "Date: "+datetime.now().strftime("%a, %d %b %y %H:%M:%S %Z")

        if self.connection_alive:
            self.headers['connection'] = "Connection: keep-alive"
        else:
            self.headers['connection'] = "Connection: close"
        self.headers['server'] = "Server: "+self.server
        self.headers['access-control-allow-origin'] = "Access-Control-Allow-Origin: "+self.allow_origin
        if self.accept_ranges:
            self.headers['accept-ranges'] = "Accept-Ranges: "+self.accept_ranges
        if self.body:
            self.headers['content-type'] = "Content-Type: "+self.content_type
            self.headers['content-length'] = "Content-Length: "+str(self.content_length)
            self.headers['body'] = self.body
        if self.last_modified:
            self.headers['last-modified'] = "Last-Modified: "+self.last_modified
        self.is_build = True

    def get_bytes(self):
        if self.is_build:
            result = bytes()
            for header in HttpResponse.http_response_order:
                if header in self.headers:
                    # Add new line for body header
                    if header == 'body':
                        result += '\n'.encode() + self.headers[header]
                    else:
                        result += (self.headers[header] + "\n").encode()
            return result
        else:
            raise Exception("Http Response has not been build yet.")

    def __str__(self):
        if self.is_build:
            response_string = ""
            for header in HttpResponse.http_response_order:
                if header in self.headers:
                    # Add new line for body header
                    if header == 'body':
                        response_string += '\n' + str(self.headers[header])
                    else:
                        response_string += self.headers[header]+"\n"
            return response_string
        else:
            raise Exception("Http Response has not been build yet.")


class HttpResponseStatus(Enum):
    # Informational
    Continue = 100
    Switching_Protocols = 101
    Processing = 102
    # Success
    OK = 200
    Created = 201
    Accepted = 202
    Non_Authoritative_Information = 203
    No_Content = 204
    Reset_Content = 205
    Partial_Content = 206
    Multi_Status = 207
    Already_Reported = 208
    Im_Used = 226
    # Redirection
    Multiple_Choices = 300
    Moved_Permanently = 301
    Found = 302
    See_Other = 303
    Not_Modified = 304
    Use_Proxy = 305
    Switch_Proxy = 306
    Temporary_Redirect = 307
    Permanent_Redirect = 308
    # Client Errors
    Bad_Request = 400
    Unauthorized = 401
    Payment_Required = 402
    Forbidden = 403
    Not_Found = 404
    Method_Not_Allowed = 405
    Not_Acceptable = 406
    Proxy_Authentication_Required = 407
    Request_Timeout = 408
    Conflict = 409
    Gone = 410
    Length_Required = 411
    Precondition_Failed = 412
    Payload_Too_Large = 413
    URI_Too_Long = 414
    Unsupported_Media_Type = 415
    Range_Not_Satisfiable = 416
    Expectation_Failed = 417
    Misdirected_Request = 421
    Unprocessable_Entity = 422
    Locked = 423
    Failed_Dependency = 424
    Upgrade_Required = 426
    Precondition_Required = 428
    Too_Many_Requests = 429
    Request_Header_Fields_Too_Large = 431
    Unavailable_For_Legal_Reasons = 451
    # Server Errors
    Internal_Server_Error = 500
    Not_Implemented = 501
    Bad_Gateway = 502
    Service_Unavailable = 503
    Gateway_Timeout = 504
    HTTP_Version_Not_Supported = 505
    Variant_Also_Negotiates = 506
    Insufficient_Storage = 507
    Loop_Detected = 508
    Not_Extended = 510
    Network_Authentication_Required = 511

    def __str__(self):
        return str(self.name).replace("_", " ")


