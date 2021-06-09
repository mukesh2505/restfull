from rest_framework import permissions

class Isowner(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions(self,request,view ,object):
            return True
        return object.owner == request.user