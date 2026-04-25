from django.db import models


class AppUser(models.Model):
    home = models.ForeignKey(
        "core.Home",
        on_delete=models.CASCADE,
        related_name="users"
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password_hash = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_access = models.DateTimeField(null=True, blank=True)
    recovery_token = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.full_name


class Role(models.Model):
    role_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    access_level = models.IntegerField()

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.role_name


class UserRole(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="user_roles"
    )
    assignment_date = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey(
        AppUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_roles"
    )

    class Meta:
        db_table = "user_roles"
        unique_together = ("user", "role")

    def __str__(self):
        return f"{self.user} - {self.role}"


class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ("alert", "Alert"),
        ("informative", "Informative"),
        ("system", "System"),
    ]

    CHANNELS = [
        ("push", "Push"),
        ("email", "Email"),
        ("SMS", "SMS"),
        ("in_app", "In App"),
    ]

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES
    )
    title = models.CharField(max_length=150)
    message = models.TextField()
    channel = models.CharField(max_length=20, choices=CHANNELS)
    is_read = models.BooleanField(default=False)
    sent_timestamp = models.DateTimeField(auto_now_add=True)
    read_timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notifications"

    def __str__(self):
        return self.title


class SystemAudit(models.Model):
    RESULTS = [
        ("successful", "Successful"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(
        AppUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="system_audits"
    )
    action = models.CharField(max_length=100)
    affected_entity = models.CharField(max_length=50)
    affected_entity_id = models.BigIntegerField(null=True, blank=True)
    previous_value = models.JSONField(null=True, blank=True)
    new_value = models.JSONField(null=True, blank=True)
    source_ip = models.CharField(max_length=45, null=True, blank=True)
    action_timestamp = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=20, choices=RESULTS)

    class Meta:
        db_table = "system_audits"

    def __str__(self):
        return f"{self.action} - {self.result}"