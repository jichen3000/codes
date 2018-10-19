import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request, send_from_directory
from flask_socketio import SocketIO, emit, send, disconnect

from multiprocessing import Process


import time
import print_helper

import exe

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = "eventlet"
# async_mode = "threading"

app = Flask(__name__)
application = app
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, async_mode=async_mode)
socketio = SocketIO(app)
socketio.init_app(app, async_mode=async_mode, log_output=True, message_queue='redis://redis-test:6379/12')
# thread = None
# thread_lock = Lock()


process_dict = {}

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@app.route('/execution/run/<id>')
def run(id):
    print("in execution request")
    # json_data.p()
    socketio.emit('result_event', {"msg":"start..."}, namespace='/execution')
    testcase = "123"
    # cur_process = Process(target=exe.run_one_testcase, 
    #         args=(testcase, _output_func, eventlet.sleep))
    cur_process = Process(target=exe.run_one_testcase_with_process, 
            args=(testcase, _output_func, eventlet.sleep))
    cur_process.start()
    cur_process.join()

    socketio.emit('result_event', {"msg":"finished\n"}, namespace='/execution')
    return "success"

@app.route('/execution/stop/<id>')
def stop(id):
    global process_dict
    print("in stop request")
    # json_data.p()
    socketio.emit('result_event', {"msg":"stop..."}, namespace='/execution')
    testcase = "123"
    # cur_process = Process(target=exe.run_one_testcase, 
    #         args=(testcase, _output_func, eventlet.sleep))
    cur_process = process_dict[testcase]
    cur_process.p()
    if cur_process.is_alive():
        cur_process.terminate()

    socketio.emit('result_event', {"msg":"stopped\n"}, namespace='/execution')
    return "success"

@app.route('/javascripts/<path:path>')
def send_js(path):
    return send_from_directory('static/javascripts', path)

def _output_func(msg):
    msg.p()
    socketio.emit('result_event', {"msg":msg}, namespace='/execution')



# using process
@socketio.on('exec_event', namespace='/execution')
def handle_exec_event(json_data):
    global process_dict
    print("in handle_exec_event")
    print(json_data)
    # json_data.p()
    emit('result_event', {"msg":"start..."}, namespace='/execution')
    testcase = "123"
    # cur_process = Process(target=exe.run_one_testcase, 
    #         args=(testcase, _output_func, eventlet.sleep))
    cur_process = Process(target=exe.run_one_testcase_new_socketio, 
            args=(testcase, _output_func, eventlet.sleep))
    process_dict[testcase] = cur_process
    cur_process.start()
    cur_process.join()

    emit('result_event', {"msg":"finished\n"}, namespace='/execution')


# using exe    
# @socketio.on('exec_event', namespace='/execution')
# def handle_exec_event(json_data):
#     print("in handle_exec_event")
#     print(json_data)
#     # json_data.p()
#     emit('result_event', {"msg":"start..."}, namespace='/execution')
#     testcase = "123"
#     exe.run_one_testcase(testcase, _output_func, eventlet.sleep)
#     emit('result_event', {"msg":"finished\n"}, namespace='/execution')

# simple 
# @socketio.on('exec_event', namespace='/execution')
# def handle_exec_event(json_data):
#     print("in handle_exec_event")
#     print(json_data)
#     # json_data.p()
#     emit('result_event', {"msg":"start..."}, namespace='/execution')
#     for i in range(5):
#         emit('result_event', {"msg":"handle "+str(i)+"\n"}, namespace='/execution')
#         time.sleep(0.5)
#     emit('result_event', {"msg":"finished\n"}, namespace='/execution')

@socketio.on('connect', namespace='/execution')
def test_connect():
    print('execution Client connected')
    emit('result_event', {'data': 'ack'})

@socketio.on('disconnect', namespace='/execution')
def test_disconnect():
    print('execution Client disconnected')

@socketio.on_error('/execution') # handles the '/chat' namespace
def error_handler_chat(e):
    print("error_handler_chat:",e)

@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    # print(request.event["message"]) # "my error event"
    # print(request.event["args"])    # (data,)
    print("default_error_handler:",e)



