from bottle import route, run, template
# import BaseHTTPServer
import bottle
import time
#from multiprocessing import Process

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
        request_queue_size = 2
        from cherrypy import wsgiserver
        server = wsgiserver.CherryPyWSGIServer((self.host, self.port), handler)
        try:
            server.numthreads = pool_size
            server.request_queue_size = request_queue_size
            print "atom numthreads:",server._get_numthreads()
            print "atom request_queue_size:",server.request_queue_size
            server.start()
        finally:
            server.stop()    

if __name__ == '__main__':
    change_bottle_cherrypy_server()
    # cherrypy.process.plugins.Daemonizer(cherrypy.engine).subscribe()
    # t = Process(target=bottle.run(host='localhost', port=9999, server='cherrypy'))
    # t.daemon = True
    # t.start()
    # t.join()
    run(host='localhost', port=9999, server='cherrypy')
