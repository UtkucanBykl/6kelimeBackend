from rest_framework import permissions

__all__ = ['IsOwner', 'IsOwnerOrOpen']


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOrOpen(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.status == 'OPEN' and obj.publish:
            return True
        elif obj.user == request.user:
            return True
        return False
