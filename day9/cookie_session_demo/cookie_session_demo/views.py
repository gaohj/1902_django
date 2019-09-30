from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware

def index(request):
    response = HttpResponse("index首页")
    expires = datetime(year=2019,month=10,day=1,hour=20,minute=0,second=0)
    expires = make_aware(expires)
    #native时间  直到自己 几点 但是不清楚时区哪一个
    #aware时间 清楚时间  并清楚位于哪个时区
    #首先设置settings.py中的  TIME_ZONE
    response.set_cookie('user_id','abc123456',max_age=180,expires=expires,path='/cms/')
    return response
def del_cookie(request):
    response = HttpResponse('delete_cookie')
    response.delete_cookie('user_id')
    return response


def my_list(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def cms_view(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)