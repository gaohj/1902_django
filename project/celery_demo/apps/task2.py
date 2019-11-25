
from apps import app
@app.task
def cheng(x,y):
    print(x*y)
    return x*y