from rest_framework.permissions import BasePermission
from App.models import User

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user,User)