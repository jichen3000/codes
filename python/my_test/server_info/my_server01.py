from bottle import route, run, template, response, request, hook, local
import json
import time
from datetime import datetime

from server_commons import *

local.server_name = "test01"

@route('/hello/:name')
def index(name='World'):
    print 'index start'
    # start_time = datetime.now()
    do_something()
    get_other_server()
    # reset_server_info(request, response, start_time)
    print 'index end'
    return template('<b>Hello {{name}} </b>', name=name)

def get_other_server():
    import requests
    print "get_other_server"
    url = 'http://localhost:9998/hello/jc'
    req = requests.get(url)
    local.pre_headers = req.headers

def do_something(count = 1):
    for i in range(count):
        time.sleep(0.1)





run(host='localhost', port=9999)
# run(host='localhost', port=9999, server='cherrypy')