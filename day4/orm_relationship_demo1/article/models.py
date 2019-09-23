from django.db import models
from frontuser.models import FrontUser
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)

