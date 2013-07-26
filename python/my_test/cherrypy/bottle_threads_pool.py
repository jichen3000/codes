from bottle import route, run, template
# import BaseHTTPServer
import bottle
import time

@route('/hello/:name')
def index(name='World'):
    print "start %s" % name
    # time.sleep(3)
    return template('Hello {{name}}', name=name)



def change_bottle_cherrypy_server():
    bottle.server_names['cherrypy'] = AtomCherryPyServer

class AtomCherryPyServer(bottle.ServerAdapter):
    def run(self, handler): # pragma: no cover                                   
        pool_size = 1
        from cherrypy import wsgiserver
        server = wsgiserver.CherryPyWSGIServer((self.host, self.port), handler)
        try:
            server.numthreads = pool_size
            print "atom numthreads:",server._get_numthreads()
            server.start()
        finally:
            server.stop()    

if __name__ == '__main__':
    change_bottle_cherrypy_server()
    run(host='localhost', port=9999, server='cherrypy')
