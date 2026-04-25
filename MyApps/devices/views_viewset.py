from rest_framework import viewsets
from .models import IoTNode, Sensor, Actuator
from .serializers import IoTNodeSerializer, SensorSerializer, ActuatorSerializer


class IoTNodeViewSet(viewsets.ModelViewSet):
    queryset = IoTNode.objects.all()
    serializer_class = IoTNodeSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class ActuatorViewSet(viewsets.ModelViewSet):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer