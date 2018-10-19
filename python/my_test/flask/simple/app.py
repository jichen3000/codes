from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack, send_from_directory
# from ostruct import OpenStruct
from threading import Thread
from multiprocessing import Process, Queue
import time

app = Flask(__name__)

def countdown(n, q):
    q.put(1)
    while n > 0: 
        print('T-minus', n) 
        n -= 1 
        time.sleep(1)

@app.route("/")
def index():
    print(app.config)
    # return "Hello World!"
    # return app.send_static_file('index.html')
    # t = Thread(target=countdown, args=(3,))
    q = Queue()
    t = Process(target=countdown, args=(3,q))
    t.start()
    t.join()
    config = {
        "username":"admin",
        "ip": "10.160.19.45"
    }
    return render_template("index.html", config = config)

@app.route("/help")
def help():
    # return "Hello World!"
    return app.send_static_file('help.html')

@app.route('/javascripts/<path:path>')
def send_js(path):
    return send_from_directory('static/javascripts', path)

if __name__ == '__main__':
    app.run(debug=True)