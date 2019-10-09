from django.db import models

# Create your models here.

class User(models.Model):
    telephone = models.CharField(max_length=11)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
