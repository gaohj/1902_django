from django import forms
from django.core import validators
from .models import User

class MyForm(forms.Form):
    # email = forms.EmailField(label="邮箱",error_messages={"invalid":"请输入正确的邮箱"})
    email = forms.CharField(label='Email',validators=[validators.EmailValidator(message="请输入正确格式的邮箱")])
    telephone = forms.CharField(label='Tel',validators=[validators.RegexValidator(r'1[3-9]\d{9}',message="请输入正确格式的手机号码")])
    price = forms.FloatField(label="价格",max_value=20,error_messages={"invalid":"请输入浮点的类型","max_value":"最大值不能超过10"})
    personal_website = forms.URLField(label="个人主页",error_messages={"invalid":"请输入正确的个人网站","required":"请输入网站"})

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3-9]\d{9}',message='请输入正确格式的手机号码')])
    pwd1 = forms.CharField(max_length=50,min_length=6)
    pwd2 = forms.CharField(max_length=50,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        res = User.objects.filter(telephone=telephone).exists()
        if res:
            raise forms.ValidationError(message="%s已经被注册" % telephone)
        return telephone
    #走到clean 方法 说明之前的 字段都验证成功了
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message="两次密码输入不一致")
        return cleaned_data