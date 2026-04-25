from django.contrib import admin
from .models import AppUser, Role, UserRole, Notification, SystemAudit


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "home", "is_active")
    search_fields = ("full_name", "email")
    list_filter = ("is_active",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "role_name", "access_level")
    search_fields = ("role_name",)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "role", "assignment_date")
    list_filter = ("role",)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "title", "notification_type", "is_read")
    list_filter = ("notification_type", "is_read")
    search_fields = ("title", "message")


@admin.register(SystemAudit)
class SystemAuditAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "action", "result", "action_timestamp")
    list_filter = ("result",)
    search_fields = ("action", "affected_entity")