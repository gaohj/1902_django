import os
from django.db import models
from django.core import validators
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnail = models.FileField(upload_to=os.path.join(os.path.dirname(os.path.dirname(__file__)),'files'),validators=[validators.FileExtensionValidator(['txt','zip'],message="必须是图片类型的文件")])
    # thumbnail = models.ImageField(upload_to='files')
    thumbnail = models.ImageField(upload_to='%Y/%m/%d')
