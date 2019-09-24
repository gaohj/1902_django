from django.db import models

# Create your models here.
#varchar  char
class FrontUser(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return "<FrontUser:(id:%s,username:%s)>" % (self.id, self.username)

class UserExtension(models.Model):
    cardid = models.IntegerField()
    user = models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name="extensions")

    def __str__(self):
        return "<UserExtension:(id:%s,cardid:%s,user_id:%s)>" % (self.id, self.cardid,self.user.id)



