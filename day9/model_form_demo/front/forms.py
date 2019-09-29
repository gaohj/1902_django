from django import forms
from .models import Article

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