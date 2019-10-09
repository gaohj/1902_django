from .models import User

#get_response 是个方法
def front_user_middleware(get_response):
    #执行一些初始化的代码
    print('哥在这里只是做一些初始化的工作')
    def middleware(request):#真正执行的是在这里
        print('request到达view试图函数之前执行的代码')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None



        #这上面的代码 是request 到达view之前的代码
        response = get_response(request) #这是一个界限
        print('reponse到达浏览器之前执行的代码')
        return response
    return middleware

