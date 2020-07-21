from rest_framework.permissions import BasePermission

class IsSuper(BasePermission):
    message = " You must be the superuser"
    def has_permission(self, request, view):
        return request.user.is_superuser