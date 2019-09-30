from django import forms
from .models import Article,User

class AddArticleForm(forms.ModelForm):
    def clean_word_num(self):
        word_num = self.cleaned_data.get('word_num')
        if word_num>100:
            raise forms.ValidationError('总词数不能超过100个')
        return word_num
    class Meta:
        model = Article
        fields = "__all__" #使用model中的所有的字段
        #exclude = ['word_num'] #排除指定的字段
        #fields = ['title','content','price'] #指定的字段
        error_messages = {
            'word_num':{
                'required':'请传入word_num参数',
                'invalid':'请输入正确的请传入word_num参数'
            },
            'title': {
                'max_length': 'title最大不能超过100个字符',
            },
            'price': {
                'max_value': '文章价格不能超过100元',
            },

        }

class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)

    #只要是走到这里说明 字段都验证成功了
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码输入不一致")
        return cleaned_data
    class Meta:
        model = User
        exclude = ['password']