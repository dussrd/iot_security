from rest_framework import viewsets
from .models import AppUser, Role, UserRole, Notification, SystemAudit
from .serializers import (
    AppUserSerializer,
    RoleSerializer,
    UserRoleSerializer,
    NotificationSerializer,
    SystemAuditSerializer
)


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


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