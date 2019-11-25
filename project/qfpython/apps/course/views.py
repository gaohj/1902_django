from django.shortcuts import render
import os,hmac,hashlib,time
from django.conf import settings
from utils import restful
from .models import Course
# Create your views here.
#生成token 发给前端
def course_index(request):
    context = {
        'courses':Course.objects.all()
    }

    return render(request,'course/course_index.html',context=context)

def course_detail(request,course_id):
    course = Course.objects.get(pk=course_id)
    context = {
        'course':course
    }
    return render(request, 'course/course_detail.html', context=context)


def course_token(request):
    file = request.GET.get('video') #从前端接收url地址

    expiration_time = int(time.time()) + 2 * 60 * 60 #过期时间

    USER_ID = settings.BAIDU_CLOUD_USERID  #userid
    USER_KEY = settings.BAIDU_CLOUD_USE_KEY #user_key

    extension = os.path.splitext(file)[1] #从url地址中截取
    media_id = file.split('/')[-1].replace(extension, '')
    #获取唯一media_id

    key = USER_KEY.encode('utf-8')
    message = '/{0}/{1}'.format(media_id, expiration_time).encode('utf-8')
    signature = hmac.new(key, message, digestmod=hashlib.sha256).hexdigest()
    token = '{0}_{1}_{2}'.format(signature, USER_ID, expiration_time)
    return restful.result(data={'token': token})