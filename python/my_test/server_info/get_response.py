import requests
import json

from server_commons import get_server_infos

def show_server_infos(server_infos):
    for index, server_info in enumerate(reversed(server_infos)):
        print "Server %d(%s)" % (index, server_info['name'])


url = 'http://localhost:9999/hello/jc'
# server_info_1 = {'name':'test-one'}
# headers = {'server-num': '1', 'server-info-0': json.dumps(server_info_1) }
# r=requests.get(url, headers=headers)
r = requests.get(url)
# print r.headers['server-num']

server_num, server_infos = get_server_infos(r.headers)
print 'server_num:',server_num
# print 'server_infos:',server_infos
show_server_infos(server_infos)




# use the json as content

if __name__ == '__main__':
    from minitest import *