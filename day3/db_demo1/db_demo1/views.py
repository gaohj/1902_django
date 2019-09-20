from django.shortcuts import render
from django.db import connection
def index(request):
    #创建 连接实例
    cursor = connection.cursor()
    #准备sql语句 并且执行
    cursor.execute("select * from users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request,'index.html')