from django.db import models

# Create your models here.
class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=1)



class Game(models.Model):
    g_name = models.CharField(max_length=32)
    g_price = models.FloatField(default=1)


class Movie(models.Model):
    m_name = models.CharField(max_length=32)
    m_price = models.FloatField(default=1)