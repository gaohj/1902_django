import time
from celery import  Celery

app = Celery('celery_test',broker='redis://localhost:6379/1',backend='redis://localhost:6379/2')

@app.task
def hello(name):
    time.sleep(4)
    print('hello:{}'.format(name))
    return 'hello world:{}'.format(name)


@app.task
def my_task(x,y):
    print(x+y)
    return x+y
