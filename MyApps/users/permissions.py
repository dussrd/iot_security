from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAppAdminOrReadOnly(BasePermission):
    message = "Solo los usuarios con rol admin pueden modificar esta ruta."

    def has_permission(self, request, view):
        user = getattr(request, "user", None)

        if not user or not getattr(user, "is_authenticated", False):
            return False

        if request.method in SAFE_METHODS:
            return True

        return getattr(user, "is_app_admin", False)
