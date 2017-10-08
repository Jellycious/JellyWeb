from HttpResponse import *


def get_internal_server_error():
    r = HttpResponse(HttpResponseStatus(500))
    r.build()
    return r

