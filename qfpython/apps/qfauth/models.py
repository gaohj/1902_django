from django.db import models
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):

    def _create_user(self, telephone,username,password, **kwargs):
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('The given password must be set')
        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone,username,password,**kwargs):
        kwargs['is_superuser']=False
        return self._create_user(telephone,username,password, **kwargs)

    def create_superuser(self, telephone,username,password,**kwargs):
        kwargs['is_superuser']=True
        kwargs['is_staff']=True
        return self._create_user(telephone,username,password, **kwargs)



class User(AbstractBaseUser,PermissionsMixin):
    #pip install django-shortuuidfield 不使用自增主键  使用shortuuid
    #容易暴露隐私
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True,null=True)
    username = models.CharField(unique=True,max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username