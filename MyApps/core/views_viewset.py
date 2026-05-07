from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Home, HomeZone, SensorReading, MotionEvent, SystemAlert
from .serializers import (
    HomeSerializer,
    HomeZoneSerializer,
    SensorReadingSerializer,
    MotionEventSerializer,
    SystemAlertSerializer
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


class HomeViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomeZoneViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    queryset = HomeZone.objects.all()
    serializer_class = HomeZoneSerializer


class SensorReadingViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer


class MotionEventViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    queryset = MotionEvent.objects.all()
    serializer_class = MotionEventSerializer


class SystemAlertViewSet(LimitedUserPatchMixin, viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    allowed_write_roles = ("lector", "operador")
    allowed_write_methods = ("PATCH",)
    allowed_user_patch_fields = ("is_resolved", "resolution_timestamp")
    queryset = SystemAlert.objects.all()
    serializer_class = SystemAlertSerializer
