import eventlet
eventlet.monkey_patch()

from threading import Lock
from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit, send, disconnect


import time
import print_helper

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = "eventlet"
# async_mode = "threading"

app = Flask(__name__)
application = app
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
# thread = None
# thread_lock = Lock()




@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/javascripts/<path:path>')
def send_js(path):
    return send_from_directory('static/javascripts', path)

@socketio.on('exec_event', namespace='/execution')
def handle_exec_event(json_data):
    print("in handle_exec_event")
    print(json_data)
    # json_data.p()
    emit('result_event', {"msg":"start..."}, namespace='/execution')
    for i in range(10):
        emit('result_event', {"msg":"handle "+str(i)+"\n"}, namespace='/execution')
        time.sleep(1)
    emit('close_event', {"msg":"close\n"}, namespace='/execution')

@socketio.on('connect', namespace='/execution')
def test_connect():
    print('execution Client connected')
    emit('result_event', {'data': 'ack'})

@socketio.on('disconnect', namespace='/execution')
def test_disconnect():
    print('execution Client disconnected')

@socketio.on_error('/execution') # handles the '/chat' namespace
def error_handler_chat(e):
    print(e)

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    # print(request.event["message"]) # "my error event"
    # print(request.event["args"])    # (data,)
    print(e)

if __name__ == '__main__':
    socketio.run(app, port=5001, debug=True, log_output=True)


