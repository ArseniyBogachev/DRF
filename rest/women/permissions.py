from rest_framework import permissions
from .models import BlackListJWT


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


class TokenIsInvalid(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user.id
        jwt_token = True
        try:
            black_list = BlackListJWT.objects.get(user=user, token=request.auth)

            if black_list:
                jwt_token = False
        except:
            jwt_token = True

        return jwt_token