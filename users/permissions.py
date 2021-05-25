from rest_framework.permissions import BasePermission

class usersPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        else:
            return request.user.is_superuser