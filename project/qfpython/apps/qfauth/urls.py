from django.urls import path
from . import views


app_name = 'qfauth'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('img_captcha/',views.img_captcha,name='img_captcha'),
    path('sms_captcha/',views.sms_captcha,name='sms_captcha'),
]