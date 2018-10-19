import time

from flask import Flask  
from flask import url_for

from celery import Celery  
from celery.result import AsyncResult  
import celery.states as states


CELERY_BROKER_URL='redis://redis-test:6379/13' 
CELERY_RESULT_BACKEND='redis://redis-test:6379/13'

celery= Celery('tasks',  
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

app = Flask(__name__)

# Send two numbers to add
@app.route('/add/<int:param1>/<int:param2>')
def add(param1,param2):  
    task = celery.send_task('mytasks.add', args=[param1, param2])
    return task.id

# Check the status of the task with the id found in the add function
@app.route('/check/<string:id>')
def check_task(id):  
    res = celery.AsyncResult(id)
    return res.state if res.state==states.PENDING else str(res.result)

@app.route('/command/<cmd_str>')
def exec_command(cmd_str):  
    task = celery.send_task('mytasks.exec_command', args=[cmd_str])
    for i in range(1000):
        res = celery.AsyncResult(task.id)
        print(i, res.info)
        time.sleep(1)
        if res.state != "PROGRESS":
            break

    return task.id

if __name__ == '__main__':  
    app.run(debug=True,
            port=5000,
            host='0.0.0.0')
