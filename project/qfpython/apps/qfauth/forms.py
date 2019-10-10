from django import forms
from apps.forms import FormMixin


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
        return cleaned_data