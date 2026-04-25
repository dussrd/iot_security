from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class AutomationSetting(models.Model):
    OPERATORS = [
        ("<", "<"),
        (">", ">"),
        ("=", "="),
        (">=", ">="),
        ("<=", "<="),
    ]

    ACTIONS = [
        ("turn_on", "Turn On"),
        ("turn_off", "Turn Off"),
        ("toggle", "Toggle"),
    ]

    home = models.ForeignKey(
        "core.Home",
        on_delete=models.CASCADE,
        related_name="automation_settings"
    )
    rule_name = models.CharField(max_length=150)
    condition_sensor = models.ForeignKey(
        "devices.Sensor",
        on_delete=models.CASCADE,
        related_name="automation_conditions"
    )
    condition_operator = models.CharField(max_length=5, choices=OPERATORS)
    condition_value = models.DecimalField(max_digits=10, decimal_places=4)
    action_actuator = models.ForeignKey(
        "devices.Actuator",
        on_delete=models.CASCADE,
        related_name="automation_actions"
    )
    action = models.CharField(max_length=20, choices=ACTIONS)
    is_active = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)

    class Meta:
        db_table = "automation_settings"

    def __str__(self):
        return self.rule_name


class LightingStatus(models.Model):
    STATUS_CHOICES = [
        ("on", "On"),
        ("off", "Off"),
        ("dimmed", "Dimmed"),
    ]

    CHANGE_SOURCES = [
        ("automatic", "Automatic"),
        ("manual", "Manual"),
        ("scheduled", "Scheduled"),
    ]

    actuator = models.ForeignKey(
        "devices.Actuator",
        on_delete=models.CASCADE,
        related_name="lighting_statuses"
    )
    zone = models.ForeignKey(
        "core.HomeZone",
        on_delete=models.CASCADE,
        related_name="lighting_statuses"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    intensity_percentage = models.IntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    change_timestamp = models.DateTimeField(auto_now_add=True)
    change_source = models.CharField(max_length=20, choices=CHANGE_SOURCES)
    user = models.ForeignKey(
        "users.AppUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lighting_changes"
    )

    class Meta:
        db_table = "lighting_statuses"

    def __str__(self):
        return f"{self.status} - {self.intensity_percentage}%"


class AlarmStatus(models.Model):
    STATUS_CHOICES = [
        ("armed", "Armed"),
        ("disarmed", "Disarmed"),
        ("triggered", "Triggered"),
        ("silenced", "Silenced"),
    ]

    home = models.ForeignKey(
        "core.Home",
        on_delete=models.CASCADE,
        related_name="alarm_statuses"
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    change_timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.AppUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="alarm_changes"
    )
    reason = models.CharField(max_length=255, null=True, blank=True)
    access_code_hash = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "alarm_statuses"

    def __str__(self):
        return self.status


class RemoteCommand(models.Model):
    CHANNELS = [
        ("REST_API", "REST API"),
        ("MQTT", "MQTT"),
        ("mobile_app", "Mobile App"),
    ]

    SENDING_STATUS = [
        ("pending", "Pending"),
        ("sent", "Sent"),
        ("failed", "Failed"),
    ]

    user = models.ForeignKey(
        "users.AppUser",
        on_delete=models.CASCADE,
        related_name="remote_commands"
    )
    actuator = models.ForeignKey(
        "devices.Actuator",
        on_delete=models.CASCADE,
        related_name="remote_commands"
    )
    command_type = models.CharField(max_length=50)
    json_parameters = models.JSONField(null=True, blank=True)
    sent_timestamp = models.DateTimeField(auto_now_add=True)
    sending_channel = models.CharField(max_length=20, choices=CHANNELS)
    sending_status = models.CharField(
        max_length=20,
        choices=SENDING_STATUS,
        default="pending"
    )

    class Meta:
        db_table = "remote_commands"

    def __str__(self):
        return self.command_type


class CommandResponse(models.Model):
    command = models.OneToOneField(
        RemoteCommand,
        on_delete=models.CASCADE,
        related_name="response"
    )
    response_timestamp = models.DateTimeField(auto_now_add=True)
    was_successful = models.BooleanField()
    response_message = models.CharField(max_length=255, null=True, blank=True)
    resulting_actuator_status = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "command_responses"

    def __str__(self):
        return f"Response for command {self.command.id}"