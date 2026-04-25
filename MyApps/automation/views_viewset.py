from rest_framework import viewsets
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


class AutomationSettingViewSet(viewsets.ModelViewSet):
    queryset = AutomationSetting.objects.all()
    serializer_class = AutomationSettingSerializer


class LightingStatusViewSet(viewsets.ModelViewSet):
    queryset = LightingStatus.objects.all()
    serializer_class = LightingStatusSerializer


class AlarmStatusViewSet(viewsets.ModelViewSet):
    queryset = AlarmStatus.objects.all()
    serializer_class = AlarmStatusSerializer


class RemoteCommandViewSet(viewsets.ModelViewSet):
    queryset = RemoteCommand.objects.all()
    serializer_class = RemoteCommandSerializer


class CommandResponseViewSet(viewsets.ModelViewSet):
    queryset = CommandResponse.objects.all()
    serializer_class = CommandResponseSerializer