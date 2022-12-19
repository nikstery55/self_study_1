from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):     # Get: 누구나, PUT/PATCH: 해당 허용 유저
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
