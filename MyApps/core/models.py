from django.db import models

# Create your models here.
from django.db import models


class Home(models.Model):
    home_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Colombia")
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "homes"

    def __str__(self):
        return self.home_name


class HomeZone(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="zones")
    zone_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    floor_number = models.IntegerField(default=1)

    class Meta:
        db_table = "home_zones"

    def __str__(self):
        return self.zone_name


class SensorReading(models.Model):
    sensor = models.ForeignKey(
        "devices.Sensor",
        on_delete=models.CASCADE,
        related_name="readings"
    )
    value = models.DecimalField(max_digits=10, decimal_places=4)
    text_value = models.CharField(max_length=50, null=True, blank=True)
    reading_timestamp = models.DateTimeField(auto_now_add=True)
    signal_quality = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "sensor_readings"

    def __str__(self):
        return f"{self.sensor} - {self.value}"


class MotionEvent(models.Model):
    sensor = models.ForeignKey(
        "devices.Sensor",
        on_delete=models.CASCADE,
        related_name="motion_events"
    )
    zone = models.ForeignKey(
        HomeZone,
        on_delete=models.CASCADE,
        related_name="motion_events"
    )
    event_timestamp = models.DateTimeField(auto_now_add=True)
    duration_seconds = models.IntegerField(null=True, blank=True)
    confidence_level = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_processed = models.BooleanField(default=False)

    class Meta:
        db_table = "motion_events"

    def __str__(self):
        return f"Motion event in {self.zone}"


class SystemAlert(models.Model):
    ALERT_TYPES = [
        ("motion", "Motion"),
        ("luminosity", "Luminosity"),
        ("connection", "Connection"),
        ("hardware", "Hardware"),
        ("security", "Security"),
    ]

    SEVERITY_LEVELS = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
        ("critical", "Critical"),
    ]

    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name="alerts")
    sensor = models.ForeignKey(
        "devices.Sensor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="alerts"
    )
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    severity_level = models.CharField(max_length=20, choices=SEVERITY_LEVELS)
    description = models.TextField()
    alert_timestamp = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    resolution_timestamp = models.DateTimeField(null=True, blank=True)
    resolved_by = models.ForeignKey(
        "users.AppUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="resolved_alerts"
    )

    class Meta:
        db_table = "system_alerts"

    def __str__(self):
        return f"{self.alert_type} - {self.severity_level}"