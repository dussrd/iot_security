from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import IoTNode, Sensor, Actuator
from .serializers import IoTNodeSerializer, SensorSerializer, ActuatorSerializer


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


class IoTNodeViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    queryset = IoTNode.objects.all()
    serializer_class = IoTNodeSerializer


class SensorViewSet(viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ActuatorViewSet(LimitedUserPatchMixin, viewsets.ModelViewSet):
    allowed_read_roles = ("lector", "operador")
    allowed_write_roles = ("operador",)
    allowed_write_methods = ("PATCH",)
    allowed_user_patch_fields = ("current_status", "operation_mode", "is_active")
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
