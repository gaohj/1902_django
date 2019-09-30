from django.db import models
from django.core import validators

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    word_num = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=100)])

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    telephone = models.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3-9]\d{9}')])
