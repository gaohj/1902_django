
from apps import app
@app.task
def add(x,y,name):
    print(x+y)
    print(name)
    return x+y

@app.task(queue='task2_q')
def sum(x,y):
    print(x+y)
    return x+y