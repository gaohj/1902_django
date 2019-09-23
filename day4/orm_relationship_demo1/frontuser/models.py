from django.db import models

# Create your models here.
#varchar  char
class FrontUser(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return "<FrontUser:(id:%s,username:%s)>" % (self.id, self.username)




