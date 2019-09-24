from django.db import models
from frontuser.models import FrontUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True)
    tag_set = models.ManyToManyField("Tag", related_name="articles")
    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id, self.title)
class Tag(models.Model):
    name = models.CharField(max_length=50)
    #articles = models.ManyToManyField("Article",related_name="tags")

    def __str__(self):
        return "<Tag:(id:%s,name:%s)>" % (self.id, self.name)
#自动会创建中间表  表中有三个字段  id  article_id  tag_id