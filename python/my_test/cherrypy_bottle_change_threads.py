from bottle import route, run, template
# import BaseHTTPServer
import bottle

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}} </b>', name=name)

class AtomCherryPyServer(bottle.ServerAdapter):
    def run(self, handler): # pragma: no cover                                   
        from cherrypy import wsgiserver
        print "ATOM"
        server = wsgiserver.CherryPyWSGIServer((self.host, self.port), handler)
        try:
            server.numthreads = 3
            print "bo numthreads:",server._get_numthreads()
            server.start()
        finally:
            server.stop()

bottle.server_names['cherrypy'] = AtomCherryPyServer
print "server_names:",bottle.server_names['cherrypy']



run(host='localhost', port=9999, server='cherrypy')
