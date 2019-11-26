import time
from apps import app

@app.task
def beat_test(x,y,name):
    time.sleep(4)
    print(x*y)
    print(name)
    return 'hello celery beat'