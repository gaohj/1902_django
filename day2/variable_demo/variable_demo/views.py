from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username = username

# def index(request):
#     p = Person("guodong兄")
#     context = {
#         'person':p
#     }
#     return render(request,'index.html',context=context)

# def index(request):
#     context = {
#         'person':{
#             'username':'kangbazi',
#             'age':18
#         }
#     }
#     return render(request,'index.html',context=context)

# def index(request):
#     context = {
#         'person':(
#             '张三',
#             '李四',
#             '王五'
#         )
#     }
#     return render(request,'index.html',context=context)

def index(request):
    return render(request,'index.html',context={'username':'kangbnazi'})