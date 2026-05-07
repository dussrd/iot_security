from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAppAdminOrReadOnly(BasePermission):
    message = "Solo los usuarios con rol admin pueden modificar esta ruta."

    def has_permission(self, request, view):
        user = getattr(request, "user", None)

        if not user or not getattr(user, "is_authenticated", False):
            return False

        if getattr(user, "is_app_admin", False):
            return True

        if request.method in SAFE_METHODS:
            allowed_read_roles = getattr(view, "allowed_read_roles", None)

            if allowed_read_roles is None:
                return True

            return any(user.has_role(role) for role in allowed_read_roles)

        allowed_write_roles = getattr(view, "allowed_write_roles", None)
        allowed_write_methods = getattr(view, "allowed_write_methods", ("PATCH",))

        if allowed_write_roles and request.method in allowed_write_methods:
            return any(user.has_role(role) for role in allowed_write_roles)

        return False
