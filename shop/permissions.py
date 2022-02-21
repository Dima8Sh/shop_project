from rest_framework import permissions


class CategoryPermissions(permissions.BasePermission):

    def has_permissions(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class ProductPermissions(permissions.BasePermission):

    def has_user_permissions(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


class BrandPermissions(permissions.BasePermission):

    def has_user_permissions(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
