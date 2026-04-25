from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_viewset import (
    HomeViewSet,
    HomeZoneViewSet,
    SensorReadingViewSet,
    MotionEventViewSet,
    SystemAlertViewSet
)

router = DefaultRouter()
router.register(r'homes', HomeViewSet)
router.register(r'zones', HomeZoneViewSet)
router.register(r'sensor-readings', SensorReadingViewSet)
router.register(r'motion-events', MotionEventViewSet)
router.register(r'system-alerts', SystemAlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]