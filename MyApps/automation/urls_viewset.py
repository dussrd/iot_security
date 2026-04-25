from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_viewset import (
    AutomationSettingViewSet,
    LightingStatusViewSet,
    AlarmStatusViewSet,
    RemoteCommandViewSet,
    CommandResponseViewSet
)

router = DefaultRouter()
router.register(r'automation-settings', AutomationSettingViewSet)
router.register(r'lighting-statuses', LightingStatusViewSet)
router.register(r'alarm-statuses', AlarmStatusViewSet)
router.register(r'remote-commands', RemoteCommandViewSet)
router.register(r'command-responses', CommandResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]