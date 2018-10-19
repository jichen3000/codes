# gunicorn --bind 0.0.0.0:5001 wsgi
# gunicorn --worker-class eventlet -w 1 --bind 0.0.0.0:5001 wsgi
# where is the logs?
from app import app as application
# from app import socketio as application
# https://github.com/xarg/flask-socketio-eventlet-example

# if __name__ == '__main__':
#     app.run()