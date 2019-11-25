
from apps import app
@app.task
def add(x,y,name):
    print(x+y)
    print(name)
    return x+y