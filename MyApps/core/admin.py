from django.contrib import admin
from .models import Home, HomeZone, SensorReading, MotionEvent, SystemAlert


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ("id", "home_name", "city", "is_active", "registration_date")
    search_fields = ("home_name", "city", "address")
    list_filter = ("is_active", "city")


@admin.register(HomeZone)
class HomeZoneAdmin(admin.ModelAdmin):
    list_display = ("id", "zone_name", "home", "floor_number")
    search_fields = ("zone_name",)
    list_filter = ("home",)


@admin.register(SensorReading)
class SensorReadingAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "value", "reading_timestamp")
    search_fields = ("sensor__sensor_name",)
    list_filter = ("reading_timestamp",)


@admin.register(MotionEvent)
class MotionEventAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor", "zone", "event_timestamp", "is_processed")
    list_filter = ("is_processed", "event_timestamp")


@admin.register(SystemAlert)
class SystemAlertAdmin(admin.ModelAdmin):
    list_display = ("id", "alert_type", "severity_level", "home", "is_resolved")
    list_filter = ("alert_type", "severity_level", "is_resolved")
    search_fields = ("description",)