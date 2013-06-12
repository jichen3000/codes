from bottle import route, run, template
# import BaseHTTPServer

@route('/hello/:name')
def index(name='World'):
	return template('<b>Hello {{name}} </b>', name=name)

# from cherrypy import wsgiserver
# setattr(cherrypy.server.httpserver,'allow_reuse_address',0)
#run(host='localhost', port=9999)
run(host='localhost', port=9999, server='cherrypy')