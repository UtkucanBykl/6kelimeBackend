from rest_framework import permissions

__all__ = ['IsOwner']


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
