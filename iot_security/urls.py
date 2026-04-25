"""
URL configuration for iot_security project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("pir_events/", include("MyApps.pir_events.urls")),
    # path("ldr_readings/", include("MyApps.ldr_readings.urls")),
    # path("devices/", include("MyApps.devices.urls")),
    # path("actuator_statuses/", include("MyApps.actuator_statuses.urls")),
    
    path('api/core/', include('MyApps.core.urls_viewset')),
    path('api/devices/', include('MyApps.devices.urls_viewset')),
    path('api/automation/', include('MyApps.automation.urls_viewset')),
    path('api/users/', include('MyApps.users.urls_viewset')),
]
