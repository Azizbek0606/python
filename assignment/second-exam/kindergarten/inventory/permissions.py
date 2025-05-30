from rest_framework.permissions import BasePermission


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role.role in ["admin", "manager"]
            if hasattr(request.user, "role")
            else False
        )


class IsAdminOrChef(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role.role in ["admin", "chef"]
            if hasattr(request.user, "role")
            else False
        )
