from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50,null=False)
    author = models.CharField(max_length=50,null=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return "<Book:({name},{author},{price})>" .format(name=self.name,author=self.author,price=self.price)


