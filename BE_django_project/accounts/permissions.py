# users/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserRole(BasePermission):
    """
    Allow only users with role=admin to perform certain actions.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.role == 'admin' or request.user.is_superuser)
