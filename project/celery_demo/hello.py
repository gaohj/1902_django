from task import hello,my_task


from apps.task1 import add
from apps.task2 import cheng
if __name__ == "__main__":
    # hello.delay()
    # hello.delay('kangbazi')
    # my_task.delay(5,6)
    # add.delay(6,8)
    add.apply_async(args=[6,6],kwargs={'name':'kangbazi'})
    cheng.delay(10,20)
