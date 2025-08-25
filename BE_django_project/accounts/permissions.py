from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserRole(BasePermission):
    """
    Allow only users with role=admin to perform certain actions.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and (request.user.role == 'admin' or request.user.is_superuser)


class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission: only review owner or admin can edit/delete.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Write permissions: only the owner or an admin/superuser
        return obj.user == request.user or request.user.role == 'admin' or request.user.is_superuser