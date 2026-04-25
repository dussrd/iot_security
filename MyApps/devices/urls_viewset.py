from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_viewset import IoTNodeViewSet, SensorViewSet, ActuatorViewSet

router = DefaultRouter()
router.register(r'nodes', IoTNodeViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'actuators', ActuatorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]