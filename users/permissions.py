from rest_framework.permissions import BasePermission

# Permissions for user roles in the library system
class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "librarian")

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "student")

