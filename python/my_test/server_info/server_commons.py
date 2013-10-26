from bottle import response, request, hook, local
import json
import time
from datetime import datetime


SERVER_NUM = 'server-num'
SERVER_INFO_PREFIX = 'server-info-'

@hook('before_request')
def before_all():
    print 'before_request'
    local.app_start_time = datetime.now()
    local.pre_headers = None

@hook('after_request')
def after_all():
    print 'after_request'
    reset_server_info(response, local.app_start_time)


def reset_server_info(response, start_time):
    if local.pre_headers:
        server_num, server_infos = get_server_infos(local.pre_headers)
    else:
        server_num = 0 
        server_infos = []
        print "no"


    cur_server_info = {
                        'name':local.server_name, 
                        'start-time':start_time.isoformat(),
                        'end-time':datetime.now().isoformat()}
    server_infos.append(cur_server_info)
    # server_num = len(server_infos)

    return set_server_infos(response.set_header, server_infos)

def get_server_infos(request_headers):
    server_num = 0
    if SERVER_NUM in request_headers:
        server_num = int(request_headers.get(SERVER_NUM))
    server_infos = [ json.loads(request_headers.get(SERVER_INFO_PREFIX+str(i))) for i in range(server_num)]
    return server_num, server_infos

def set_server_infos(set_header_func, server_infos):
    set_header_func(SERVER_NUM, str(len(server_infos)))
    [set_header_func(SERVER_INFO_PREFIX+str(index), json.dumps(info)) 
            for index, info in enumerate(server_infos)]
        
    return len(server_infos)

