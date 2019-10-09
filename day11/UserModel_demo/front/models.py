from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
#User.objects.all()
#Person.objects.all()  #实际上就是User在执行  不影响User的情况下 添加新的操作
#Person是 User的代理 以上两个就是等同的
#在代理模型中不能添加字段
# class Person(User):
#     class Meta:
#         proxy = True #表明立场 我是User模型的代理
#
#     @classmethod
#     def get_black_list(cls):
#         return cls.objects.filter(is_active=False)


class UserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
    telephone = models.CharField(max_length=11)
    school = models.CharField(max_length=100)

    #如果User模型 新建了一个用户或者修改用户信息   要通知扩展模型
    #判断 是否是新建 还是 修改
    @receiver(post_save,sender=User)
    def handler_user_extension(sender,instance,created,**kwargs):
        if created:
            UserExtension.objects.create(user=instance)
        else:
            instance.extension.save()
