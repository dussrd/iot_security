from django.contrib import admin
from .models import (
    AutomationSetting,
    LightingStatus,
    AlarmStatus,
    RemoteCommand,
    CommandResponse
)


@admin.register(AutomationSetting)
class AutomationSettingAdmin(admin.ModelAdmin):
    list_display = ("id", "rule_name", "home", "is_active", "priority")
    search_fields = ("rule_name",)
    list_filter = ("is_active", "priority")


@admin.register(LightingStatus)
class LightingStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "actuator", "zone", "status", "intensity_percentage")
    list_filter = ("status", "change_source")


@admin.register(AlarmStatus)
class AlarmStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "home", "status", "change_timestamp")
    list_filter = ("status",)


@admin.register(RemoteCommand)
class RemoteCommandAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "actuator", "command_type", "sending_status")
    list_filter = ("sending_status", "sending_channel")
    search_fields = ("command_type",)


@admin.register(CommandResponse)
class CommandResponseAdmin(admin.ModelAdmin):
    list_display = ("id", "command", "was_successful", "response_timestamp")
    list_filter = ("was_successful",)