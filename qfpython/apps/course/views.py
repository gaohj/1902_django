from django.shortcuts import render,reverse
import os,hmac,hashlib,time
from django.conf import settings
from utils import restful
from .models import Course,CourseOrder
from hashlib import md5
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

def course_order(request,course_id):
    course = Course.objects.get(pk=course_id)
    order = CourseOrder.objects.create(course=course,buyer=request.user,status=1,amount=course.price)
    context = {
        'goods': {
            'thumbnail': course.cover_url,
            'title': course.title,
            'price': course.price,
        },
        'order': order,
        # /course/notify_url/
        'notify_url': request.build_absolute_uri(reverse('course:notify_view')),
        'return_url': request.build_absolute_uri(reverse('course:course_detail',kwargs={"course_id":course.pk}))
    }
    return render(request,'course/course_order.html',context=context)

def course_order_key(request):
    goodsname = request.POST.get('goodsname')
    istype = request.POST.get('istype')
    notify_url= request.POST.get('notify_url')
    orderid= request.POST.get('orderid')
    orderuid= str(request.user.pk) #当前登录用户的唯一id
    price = request.POST.get('price')
    return_url = request.POST.get('return_url')
    token = '38d65a70d204d02914020bbdcb29ce4a'
    uid = '0f1b04d1051c0b3521e108a4'
    key = md5((goodsname + istype + notify_url + orderid + orderuid + price + return_url + token + uid).encode("utf-8")).hexdigest()
    return restful.result(data={'key':key})

def notify_view(request):
    order_id = request.POST.get('orderid')
    print("="*50)
    print(order_id)
    print("="*50)

    CourseOrder.objects.filter(pk=order_id).update(status=2)
    return restful.success()

