from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'category'
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True)
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id, self.title)

    class Meta:
        db_table = 'article'

