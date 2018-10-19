import gevent
from gevent import monkey
monkey.patch_all()

import os
from flask import Flask, render_template, Response
from flask_sse import sse
from time import sleep
from multiprocessing import Process, Queue
from threading import Thread

import print_helper

import exe

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://redis-test:6379/12"
app.register_blueprint(sse, url_prefix='/stream')

process_dict = {}

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/command_worker/run/<id>')
# def command_run(id):
#     global process_dict
#     "command_run".p()
#     # sse.publish("work {} start... ".format(id), type='result')
#     sse.publish({"msg": "Hello!"}, type='result')
#     def _output(msg):
#         sse.publish({"msg": msg}, type='result')
#     def nothing(some):
#         print("nothing")
#     # sleep(1)
#     # sse.publish("1 ", type='result')
#     # exe.run_one_testcase(id, _output)
#     # cur_process = Thread(target=nothing, 
#     #             args=(id,))
#     q = Queue()
#     # cur_process = Process(target=exe.run_one_testcase2, 
#     #             args=(id, q))
#     cur_process = Thread(target=exe.new_thread, 
#                 args=(id, ))
#     process_dict[id] = cur_process
#     cur_process.start()
#     cur_process.join()
#     # cur_process = Thread(target=exe.run_one_testcase, 
#     #             args=(id, _output))
#     # # q = Queue()
#     # # cur_process = Process(target=exe.run_one_testcase2, 
#     # #             args=(id, q))
#     # cur_process.start()

#     # cur_process.join()    
#     "in1".p()
#     sse.publish({"msg": "close!"}, type='close')   
#     # resp = Response("success")
#     # resp.headers["Content-Type"] = 'text/event-stream'
#     # resp.headers["Cache-Control"] = 'no-cache'
#     # return resp
#     "in2".p()
#     return "success"
#     # 'Content-Type': 'text/event-stream',
#     # 'Cache-Control': 'no-cache',
#     # 'Connection': 'keep-alive'


@app.route('/command_worker/run/<id>')
def command_run(id):
    global process_dict
    "command_run".p()
    sse.publish({"msg": "Hello!"}, type='result')
    log_path = "output.log"
    end_str = "###allend"

    if os.path.exists(log_path):
        os.remove(log_path)
    file_ = open(log_path, "w")
    try:
        def output(msg):
            file_.write(msg)
            file_.flush()
        result = [0]
        cur_process = Thread(target=exe.func_with_file, 
                    args=(10, result, output, end_str))
        process_dict[id] = cur_process
        cur_process.start()
        # cur_process.join()

        for line in exe.tail(log_path, 0):
            # line.p()
            if line == end_str:
                sse.publish({"msg": "close!"}, type='close')
                break
            else:
                sse.publish({"msg": line}, type='result')
    finally:
        file_.close()
    "in2333".p()
    return "success"
# @app.route('/command_worker/run/<id>')
# def command_run_process(id):
#     global process_dict
#     "command_run".p()
#     sse.publish({"msg": "Hello!"}, type='result')
#     log_path = "output.log"
#     end_str = "###allend"
#     if os.path.exists(log_path):
#         os.remove(log_path)
#     file_ = open(log_path, "w")
#     try:
#         def output(msg):
#             file_.write(msg)
#             file_.flush()
#         result = [0]
#         cur_process = Process(name="inner_process", target=exe.func_with_file_for_process, 
#                     args=(10, result, output, end_str))
#         process_dict[id] = cur_process
#         cur_process.start()
#         # cur_process.join()

#         for line in exe.tail(log_path, 0):
#             # line.p()
#             if line.endswith(end_str):
#                 sse.publish({"msg": "close!"}, type='close')
#                 break
#             else:
#                 sse.publish({"msg": line}, type='result')
#     except Exception as e:
#         raise e
#     finally:
#         file_.close()
#     "in2333".p()
#     return "success"

@app.route('/command_worker/stop/<id>')
def command_stop(id):
    global process_dict
    "command_stop".p()
    if id in process_dict and process_dict[id].is_alive():
        process_dict[id].need_stop = True
        print("force stopped")
        sse.publish({"msg": "force stopped!"}, type='result')
    return "success"
# @app.route('/command_worker/stop/<id>')
# def command_stop(id):
#     global process_dict
#     "command_stop".p()
#     if id in process_dict and process_dict[id].is_alive():
#         process_dict[id].p()
#         process_dict[id].terminate()
#         print("force stopped")
#         sse.publish({"msg": "force stopped!"}, type='result')
#     return "success"



if __name__ == '__main__':
    from gevent.wsgi import WSGIServer
    app.debug = True
    app.log_output = True
    app.config["ENV"] = "development"
    # app.logger.pp()
    # app.config.pp()
    address = ('localhost', 8000)
    http_server = WSGIServer(address, app, log=app.logger)
    print("Server running on port {}:{}. Ctrl+C to quit".format(*address))

    http_server.serve_forever()
