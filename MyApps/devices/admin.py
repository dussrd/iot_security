from django.contrib import admin
from .models import IoTNode, Sensor, Actuator


@admin.register(IoTNode)
class IoTNodeAdmin(admin.ModelAdmin):
    list_display = ("id", "node_name", "zone", "connection_status", "installation_date")
    search_fields = ("node_name", "mac_address")
    list_filter = ("connection_status",)


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("id", "sensor_name", "sensor_type", "node", "is_active")
    search_fields = ("sensor_name",)
    list_filter = ("sensor_type", "is_active")


@admin.register(Actuator)
class ActuatorAdmin(admin.ModelAdmin):
    list_display = ("id", "actuator_name", "actuator_type", "node", "current_status")
    search_fields = ("actuator_name",)
    list_filter = ("actuator_type", "current_status")