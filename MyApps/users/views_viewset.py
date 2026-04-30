from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
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


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

    def get_permissions(self):
        if self.action in ("create", "login"):
            return [AllowAny()]

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


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class SystemAuditViewSet(viewsets.ModelViewSet):
    queryset = SystemAudit.objects.all()
    serializer_class = SystemAuditSerializer
