import time  
from celery import Celery

CELERY_BROKER_URL='redis://redis-test:6379/13' 
CELERY_RESULT_BACKEND='redis://redis-test:6379/13'


celery= Celery('tasks',  
                broker=CELERY_BROKER_URL,
                backend=CELERY_RESULT_BACKEND)

# The name parameter is the key here
@celery.task(name='mytasks.add')
def add(x, y):  
    time.sleep(5) # lets sleep for a while before doing the gigantic addition task!
    return x + y


@celery.task(name='mytasks.exec_command', bind=True)
def exec_command(self, cms_str): 
    for i in range(5):
        self.update_state(state='PROGRESS',
            meta={'step': i+1, 'cms_str': cms_str})
        time.sleep(4)
    return "done"

