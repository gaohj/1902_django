from django import forms
from apps.forms import FormMixin
from django.core.cache import cache
from .models import User

class LoginForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=20,min_length=6,error_messages={"max_length":"最大长度不能超过20","min_length":"最小不能少于6"})
    remember = forms.IntegerField(required=False)


class RegisterForm(forms.Form,FormMixin):
    telephone = forms.CharField(max_length=11)
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20,min_length=6,error_messages={"max_length":"最大长度不能超过20","min_length":"最小不能少于6"})
    password2 = forms.CharField(max_length=20,min_length=6,error_messages={"max_length":"最大长度不能超过20","min_length":"最小不能少于6"})
    remember = forms.IntegerField(required=False)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(message="两次密码输入不一致")

        #用户输入的图形验证码
        img_captcha = cleaned_data.get('img_captcha')
        cache_img_captcha = cache.get(img_captcha.lower())

        if not cache_img_captcha or cache_img_captcha.lower() != img_captcha.lower():
            raise forms.ValidationError(message="图形验证码错误")


        sms_captcha = cleaned_data.get('sms_captcha')
        cache_sms_captcha = cache.get(sms_captcha.lower())

        if not cache_sms_captcha or cache_sms_captcha.lower() != sms_captcha.lower():
            raise forms.ValidationError(message="短信验证码错误")

        telephone = cleaned_data.get('telephone')
        result = User.objects.filter(telephone=telephone).exists()
        if result:
            raise forms.ValidationError(message="该手机号已经存在")



        return cleaned_data