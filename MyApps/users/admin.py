from django.contrib import admin
from django import forms
from .models import AppUser, Role, UserRole, Notification, SystemAudit


class AppUserAdminForm(forms.ModelForm):
    password = forms.CharField(
        label="Contrasena",
        required=False,
        widget=forms.PasswordInput(render_value=False),
        help_text="Deja este campo vacio para conservar la contrasena actual.",
    )

    class Meta:
        model = AppUser
        fields = (
            "home",
            "full_name",
            "username",
            "email",
            "password",
            "phone",
            "is_active",
            "last_access",
            "recovery_token",
        )

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if not self.instance.pk and not password:
            raise forms.ValidationError("La contrasena es obligatoria.")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")

        if password:
            user.set_password(password)

        if commit:
            user.save()
            self.save_m2m()

        return user


class UserRoleInline(admin.TabularInline):
    model = UserRole
    extra = 1
    fk_name = "user"


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    form = AppUserAdminForm
    inlines = [UserRoleInline]
    list_display = ("id", "full_name", "username", "email", "home", "is_active")
    search_fields = ("full_name", "username", "email")
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
