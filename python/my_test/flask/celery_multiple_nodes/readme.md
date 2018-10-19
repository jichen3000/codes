# purpose
show how to use multiple nodes of Celery worker

## resource
https://moinulhossain.me/remote-celery-worker-for-flask-with-separate-code-base/

## how to run

### flask
python app.py

### celery
celery -A tasks worker --loglevel=info

### browser
http://localhost:5000/add/3/4
http://localhost:5000/command/add
