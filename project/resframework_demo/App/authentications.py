from django.core.cache import cache
from rest_framework.authentication import BasicAuthentication

from .models import User

class UserAuthentication(BasicAuthentication):
    def authenticate(self, request):
        try:
            token = request.query_params.get("token")
            user_id = cache.get(token)
            user = User.objects.get(pk=user_id)
            return user,token
        except Exception as e:
            return None