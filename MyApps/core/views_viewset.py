from rest_framework import viewsets
from .models import Home, HomeZone, SensorReading, MotionEvent, SystemAlert
from .serializers import (
    HomeSerializer,
    HomeZoneSerializer,
    SensorReadingSerializer,
    MotionEventSerializer,
    SystemAlertSerializer
)


class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomeZoneViewSet(viewsets.ModelViewSet):
    queryset = HomeZone.objects.all()
    serializer_class = HomeZoneSerializer


class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer


class MotionEventViewSet(viewsets.ModelViewSet):
    queryset = MotionEvent.objects.all()
    serializer_class = MotionEventSerializer


class SystemAlertViewSet(viewsets.ModelViewSet):
    queryset = SystemAlert.objects.all()
    serializer_class = SystemAlertSerializer