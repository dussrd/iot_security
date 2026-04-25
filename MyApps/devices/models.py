from django.db import models


class IoTNode(models.Model):
    CONNECTION_STATUS = [
        ("connected", "Connected"),
        ("disconnected", "Disconnected"),
        ("error", "Error"),
    ]

    zone = models.ForeignKey(
        "core.HomeZone",
        on_delete=models.CASCADE,
        related_name="iot_nodes"
    )
    node_name = models.CharField(max_length=100)
    hardware_type = models.CharField(max_length=50)
    mac_address = models.CharField(max_length=17, unique=True)
    local_ip = models.CharField(max_length=15, null=True, blank=True)
    firmware_version = models.CharField(max_length=20, null=True, blank=True)
    connection_status = models.CharField(
        max_length=20,
        choices=CONNECTION_STATUS,
        default="disconnected"
    )
    last_connection = models.DateTimeField(null=True, blank=True)
    installation_date = models.DateField()

    class Meta:
        db_table = "iot_nodes"

    def __str__(self):
        return self.node_name


class Sensor(models.Model):
    SENSOR_TYPES = [
        ("LDR", "LDR"),
        ("PIR", "PIR"),
        ("DHT11", "DHT11"),
        ("MQ2", "MQ2"),
        ("ultrasonic", "Ultrasonic"),
        ("other", "Other"),
    ]

    node = models.ForeignKey(
        IoTNode,
        on_delete=models.CASCADE,
        related_name="sensors"
    )
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPES)
    sensor_name = models.CharField(max_length=100)
    gpio_pin = models.CharField(max_length=10, null=True, blank=True)
    measurement_unit = models.CharField(max_length=20, null=True, blank=True)
    minimum_threshold = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    maximum_threshold = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "sensors"

    def __str__(self):
        return self.sensor_name


class Actuator(models.Model):
    ACTUATOR_TYPES = [
        ("LED", "LED"),
        ("buzzer", "Buzzer"),
        ("relay", "Relay"),
        ("motor", "Motor"),
        ("other", "Other"),
    ]

    CURRENT_STATUS = [
        ("on", "On"),
        ("off", "Off"),
        ("error", "Error"),
    ]

    OPERATION_MODES = [
        ("manual", "Manual"),
        ("automatic", "Automatic"),
    ]

    node = models.ForeignKey(
        IoTNode,
        on_delete=models.CASCADE,
        related_name="actuators"
    )
    actuator_type = models.CharField(max_length=20, choices=ACTUATOR_TYPES)
    actuator_name = models.CharField(max_length=100)
    gpio_pin = models.CharField(max_length=10, null=True, blank=True)
    current_status = models.CharField(
        max_length=20,
        choices=CURRENT_STATUS,
        default="off"
    )
    operation_mode = models.CharField(
        max_length=20,
        choices=OPERATION_MODES,
        default="manual"
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "actuators"

    def __str__(self):
        return self.actuator_name