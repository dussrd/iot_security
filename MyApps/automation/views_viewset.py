from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import (
    AutomationSetting,
    LightingStatus,
    AlarmStatus,
    RemoteCommand,
    CommandResponse
)
from .serializers import (
    AutomationSettingSerializer,
    LightingStatusSerializer,
    AlarmStatusSerializer,
    RemoteCommandSerializer,
    CommandResponseSerializer
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


class AutomationSettingViewSet(LimitedUserPatchMixin, viewsets.ModelViewSet):
    allowed_read_roles = ("operador",)
    allowed_write_roles = ("operador",)
    allowed_write_methods = ("PATCH",)
    allowed_user_patch_fields = ("is_active", "priority")
    queryset = AutomationSetting.objects.all()
    serializer_class = AutomationSettingSerializer


class LightingStatusViewSet(LimitedUserPatchMixin, viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    allowed_write_roles = ("operador",)
    allowed_write_methods = ("PATCH",)
    allowed_user_patch_fields = (
        "status",
        "intensity_percentage",
        "change_source",
        "user",
    )
    queryset = LightingStatus.objects.all()
    serializer_class = LightingStatusSerializer


class AlarmStatusViewSet(LimitedUserPatchMixin, viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    allowed_write_roles = ("operador",)
    allowed_write_methods = ("PATCH",)
    allowed_user_patch_fields = ("status", "reason", "user")
    queryset = AlarmStatus.objects.all()
    serializer_class = AlarmStatusSerializer


class RemoteCommandViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("operador",)
    queryset = RemoteCommand.objects.all()
    serializer_class = RemoteCommandSerializer


class CommandResponseViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("operador",)
    queryset = CommandResponse.objects.all()
    serializer_class = CommandResponseSerializer
