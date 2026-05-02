from django.core.exceptions import ValidationError
from django.db import models


CITY_NEIGHBORHOODS = {
    "riohacha": {
        "label": "Riohacha",
        "barrios": [
            ("centro", "Centro"),
            ("los_olivos", "Los Olivos"),
            ("cooperativo", "Cooperativo"),
            ("marbella", "Marbella"),
            ("villa_comfamiliar", "Villa Comfamiliar"),
        ],
    },
    "maicao": {
        "label": "Maicao",
        "barrios": [
            ("centro", "Centro"),
            ("san_francisco", "San Francisco"),
            ("la_floresta", "La Floresta"),
            ("el_carmen", "El Carmen"),
            ("villa_amelia", "Villa Amelia"),
        ],
    },
    "barranquilla": {
        "label": "Barranquilla",
        "barrios": [
            ("el_prado", "El Prado"),
            ("alto_prado", "Alto Prado"),
            ("riomar", "Riomar"),
            ("boston", "Boston"),
            ("ciudad_jardin", "Ciudad Jardin"),
        ],
    },
    "bogota": {
        "label": "Bogota",
        "barrios": [
            ("chapinero", "Chapinero"),
            ("usaquen", "Usaquen"),
            ("suba", "Suba"),
            ("teusaquillo", "Teusaquillo"),
            ("kennedy", "Kennedy"),
        ],
    },
    "medellin": {
        "label": "Medellin",
        "barrios": [
            ("el_poblado", "El Poblado"),
            ("laureles", "Laureles"),
            ("belen", "Belen"),
            ("robledo", "Robledo"),
            ("guayabal", "Guayabal"),
        ],
    },
}

CITY_CHOICES = [
    (city_key, city_data["label"])
    for city_key, city_data in CITY_NEIGHBORHOODS.items()
]
NEIGHBORHOOD_CHOICES = list(
    {
        neighborhood_key: neighborhood_label
        for city_data in CITY_NEIGHBORHOODS.values()
        for neighborhood_key, neighborhood_label in city_data["barrios"]
    }.items()
)


class Home(models.Model):
    home_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, choices=CITY_CHOICES, default="riohacha")
    barrio = models.CharField(max_length=100, choices=NEIGHBORHOOD_CHOICES, default="centro")
    country = models.CharField(max_length=100, default="Colombia", editable=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "homes"

    def __str__(self):
        return self.home_name

    def clean(self):
        valid_neighborhoods = {
            neighborhood_key
            for neighborhood_key, _ in CITY_NEIGHBORHOODS.get(
                self.city,
                {"barrios": []},
            )["barrios"]
        }

        if self.barrio not in valid_neighborhoods:
            raise ValidationError(
                {"barrio": "El barrio seleccionado no pertenece a la ciudad."}
            )

    def save(self, *args, **kwargs):
        self.country = "Colombia"
        self.full_clean()
        super().save(*args, **kwargs)


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
