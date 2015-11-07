class NetworkError(Exception): pass
class HostnameError(NetworkError): pass

def get_hostname_error():
    raise HostnameError("it is hostname error!")
    # e.args

class CustomError(Exception):
    def __init__(self, message, status):
        super(CustomError, self).__init__(message, status)
        self.message = message
        self.status = status
if __name__ == '__main__':
    from minitest import *

    with test(NetworkError):
        (lambda : get_hostname_error()).must_raise(
                HostnameError)