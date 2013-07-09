from bottle import route, run, template
# import BaseHTTPServer
# import bottle

@route('/hello/:name')
def index(name='World'):
    return template('<b>Hello {{name}} </b>', name=name)

# print app.conf()
run(host='localhost', port=9999, server='cherrypy')
# print server