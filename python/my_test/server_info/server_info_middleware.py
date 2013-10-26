import json
import time
from datetime import datetime


SERVER_NUM = 'server-num'
SERVER_INFO_PREFIX = 'server-info-'




def get_server_infos(request_headers):
    server_num = 0
    if SERVER_NUM in request_headers:
        server_num = int(request_headers.get(SERVER_NUM))
    server_infos = [ json.loads(request_headers.get(SERVER_INFO_PREFIX+str(i))) for i in range(server_num)]
    return server_num, server_infos

def set_server_infos(set_header_func, server_infos):
    set_header_func( (SERVER_NUM, str(len(server_infos)) ))
    [set_header_func( (SERVER_INFO_PREFIX+str(index), json.dumps(info)) ) 
            for index, info in enumerate(server_infos)]
        
    return len(server_infos)



class ServerInfoMiddleware(object):
    def __init__(self, app, server_name):
        print "init"
        self.app = app
        self.server_name = server_name

    def __call__(self, environ, start_response):
        print "call"
        self.before_request()
        # print environ
        # return self.app(environ, start_response)
        def custom_start_response(status, headers, exc_info=None):
            # headers.append(('Set-Cookie', "name=value"))
            print "custom_start_response"
            self.after_request(status, headers, exc_info)
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)

    def before_request(self):
        self.response_start_time = datetime.now()
        self.pre_headers = None

    def after_request(self, status, headers, exc_info):
        self.reset_server_info(headers)


    def set_pre_headers(self, pre_headers):
        self.pre_headers = pre_headers

    def reset_server_info(self, headers):
        if self.pre_headers:
            server_num, server_infos = get_server_infos(self.pre_headers)
        else:
            server_num = 0 
            server_infos = []
            print "no"


        cur_server_info = {
                            'name':self.server_name, 
                            'start-time':self.response_start_time.isoformat(),
                            'end-time':datetime.now().isoformat()}
        server_infos.append(cur_server_info)
        # server_num = len(server_infos)

        return set_server_infos(headers.append, server_infos)

