from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .authentication import create_auth_token
from .models import AppUser, Role, UserRole, Notification, SystemAudit
from .permissions import IsAppAdminOrReadOnly
from .serializers import (
    AppUserLoginSerializer,
    AppUserSerializer,
    RoleSerializer,
    UserRoleSerializer,
    NotificationSerializer,
    SystemAuditSerializer,
)


class LimitedUserPatchMixin:
    allowed_user_patch_fields = ()

    def partial_update(self, request, *args, **kwargs):
        user = getattr(request, "user", None)

        if user and not getattr(user, "is_app_admin", False):
            extra_fields = set(request.data) - set(self.allowed_user_patch_fields)

            if extra_fields:
                return Response(
                    {
                        "detail": "Tu rol solo permite actualizar campos operativos.",
                        "fields": sorted(extra_fields),
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

        return super().partial_update(request, *args, **kwargs)


class AppUserViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ()
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_permissions(self):
        if self.action == "login":
            return [AllowAny()]

        if self.action == "me":
            return [IsAuthenticated()]

        return [IsAppAdminOrReadOnly()]

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[AllowAny],
        authentication_classes=[],
    )
    def login(self, request):
        serializer = AppUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        user.last_access = timezone.now()
        user.save(update_fields=["last_access"])

        return Response(
            {
                "token": create_auth_token(user),
                "user": AppUserSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["get", "patch"])
    def me(self, request):
        if request.method == "GET":
            return Response(AppUserSerializer(request.user).data)

        allowed_fields = {"full_name", "username", "email", "phone", "password"}
        payload = {
            key: value
            for key, value in request.data.items()
            if key in allowed_fields
        }

        serializer = AppUserSerializer(request.user, data=payload, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class RoleViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ()
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ()
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class NotificationViewSet(LimitedUserPatchMixin, viewsets.ModelViewSet):
    allowed_read_roles = ("operador",)
    allowed_write_roles = ("lector", "operador")
    allowed_write_methods = ("PATCH",)
    allowed_user_patch_fields = ("is_read", "read_timestamp")
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class SystemAuditViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ()
    queryset = SystemAudit.objects.all()
    serializer_class = SystemAuditSerializer
