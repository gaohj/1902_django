from django.db import models
from django.core import validators

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    word_num = models.IntegerField()
    price = models.FloatField(validators=[validators.MaxValueValidator(limit_value=100)])


