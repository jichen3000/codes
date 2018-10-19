from flask import Flask

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://redis-test:6379/13',
    CELERY_RESULT_BACKEND='redis://redis-test:6379/13'
)
celery = make_celery(flask_app)

@celery.task()
def add_together(a, b):
    return a + b

if __name__ == '__main__':
    flask_app.run(debug=True)