class HttpRequest:

    def __init__(self, request_bytes):
        self.headers = {}
        self.parse_request(request_bytes)

    def parse_request(self, request_bytes):
        request_lines = request_bytes.decode().splitlines()

        if len(request_lines) > 0:

            self.headers['method'] = request_lines[0]

            for x in range(len(request_lines) - 2):
                string = request_lines[x + 1]
                string = string.split(": ")
                header = string[0].lower()
                self.headers[header] = string[1]

    def get_method(self):
        return self.headers['method'].split(" ")[0]

    def get_uri(self):
        uri = self.headers['method'].split(" ")[1]
        return uri

    def get_attribute(self, attribute_name):
        if attribute_name in self.headers:
            return self.headers[attribute_name]
        else:
            return None

    def get_headers(self):
        self.headers




