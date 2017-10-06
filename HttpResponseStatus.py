from enum import Enum


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
