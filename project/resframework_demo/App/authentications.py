from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from .models import User
class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.query_params.get('token')
            print(token)
            user_id = cache.get(token)
            print(user_id)
            user = User.objects.get(pk=user_id)

            return user,token
        except Exception as e:  #如果有错误 我们不返回
            return None
