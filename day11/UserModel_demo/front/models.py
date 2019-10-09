from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser,BaseUserManager,PermissionsMixin
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


# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)
#
#     #如果User模型 新建了一个用户或者修改用户信息   要通知扩展模型
#     #判断 是否是新建 还是 修改
#     @receiver(post_save,sender=User)
#     def handler_user_extension(sender,instance,created,**kwargs):
#         if created:
#             UserExtension.objects.create(user=instance)
#         else:
#             instance.extension.save()

class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password,email, **kwargs):
        if not telephone:
            raise ValueError('必须传手机号码')
        if not password:
            raise ValueError('必须传密码')
        user = self.model(telephone=telephone,username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone,username, password,email=None,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)

    def create_superuser(self, telephone,username, email, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)





# class User(AbstractUser):
#     telephone = models.CharField(max_length=11,unique=True)
#     school = models.CharField(max_length=50)
#
#     objects = UserManager()
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'telephone'
#     REQUIRED_FIELDS = ['email']

class User(AbstractBaseUser, PermissionsMixin):
    telephone = models.CharField(max_length=11,unique=True)
    email = models.CharField(max_length=50,unique=True)
    username = models.CharField(max_length=30,unique=True)
    is_active = models.BooleanField(default=True)


    objects = UserManager()
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username