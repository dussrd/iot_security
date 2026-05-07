from django.core.exceptions import ValidationError
from django.db import models


RIOHACHA_BARRIOS = [
    ("centro", "Centro"),
    ("barrio_arriba", "Barrio Arriba"),
    ("barrio_abajo", "Barrio Abajo"),
    ("urbanizacion_el_faro", "Urbanizacion El Faro"),
    ("san_martin_de_porres", "San Martin de Porres"),
    ("los_remedios", "Los Remedios"),
    ("el_acueducto", "El Acueducto"),
    ("el_libertador", "El Libertador"),
    ("urbanizacion_el_tatual", "Urbanizacion El Tatual"),
    ("coquivacoa", "Coquivacoa"),
    ("padilla", "Padilla"),
    ("jose_antonio_galan", "Jose Antonio Galan"),
    ("urbanizacion_sol_tropical", "Urbanizacion Sol Tropical"),
    ("urbanizacion_terrazas_de_coquivacoa", "Urbanizacion Terrazas de Coquivacoa"),
    ("paraiso", "Paraiso"),
    ("guapuna", "Guapuna"),
    ("las_mercedes", "Las Mercedes"),
    ("luis_antonio_robles", "Luis Antonio Robles"),
    ("mediterraneo_i_y_ii", "Mediterraneo I y II"),
    ("doce_de_octubre", "12 de Octubre"),
    ("marbella", "Urbanizacion Marbella"),
    ("san_tropel", "San Tropel"),
    ("nuevo_horizonte", "Nuevo Horizonte"),
    ("urbanizacion_portal_de_comfamiliar", "Urbanizacion Portal de Comfamiliar"),
    ("cooperativo", "Cooperativo"),
    ("nuevo_faro", "Nuevo Faro"),
    ("cooperativo_nuevo_faro", "Cooperativo Nuevo Faro"),
    ("la_napa", "La Napa"),
    ("edinson_deluque_pinto", "Edinson Deluque Pinto"),
    ("urbanizacion_manantial", "Urbanizacion Manantial"),
    ("urbanizacion_majayura_i_y_ii", "Urbanizacion Majayura I y II"),
    ("jorge_perez", "Jorge Perez"),
    ("cactus_i_y_ii", "Cactus I y II"),
    ("che_guevara", "Che Guevara"),
    ("las_tunas", "Las Tunas"),
    ("caribe", "Caribe"),
    ("san_martin_de_loba", "San Martin de Loba"),
    ("matajuna", "Matajuna"),
    ("aeropuerto", "Aeropuerto"),
    ("la_paz", "La Paz"),
    ("nazareth", "Nazareth"),
    ("obrero", "Obrero"),
    ("veinte_de_julio", "20 de Julio"),
    ("san_francisco", "San Francisco"),
    ("rojas_pinilla", "Rojas Pinilla"),
    ("la_loma", "La Loma"),
    ("nuestra_senora_de_los_remedios", "Nuestra Senora de los Remedios"),
    ("jose_arnoldo_marin", "Jose Arnoldo Marin"),
    ("calancala", "Calancala"),
    ("las_villas", "Las Villas"),
    ("entre_rios", "Entre Rios"),
    ("los_medanos", "Los Medanos"),
    ("el_progreso", "El Progreso"),
    ("luis_eduardo_cuellar", "Luis Eduardo Cuellar"),
    ("villa_tatiana", "Villa Tatiana"),
    ("kepiagua", "Kepiagua"),
    ("la_cosecha", "La Cosecha"),
    ("boca_grande", "Boca Grande"),
    ("los_nogales", "Los Nogales"),
    ("san_judas", "San Judas"),
    ("el_comunitario", "El Comunitario"),
    ("los_olivos", "Los Olivos"),
    ("divino_nino", "Divino Nino"),
    ("la_esperanza", "La Esperanza"),
    ("quince_de_mayo", "15 de Mayo"),
    ("comfamiliar_2000", "Comfamiliar 2000"),
    ("simon_bolivar", "Simon Bolivar"),
    ("eurare", "Eurare"),
    ("buganvilla", "Buganvilla"),
    ("camilo_torres", "Camilo Torres"),
    ("maria_eugenia_rojas", "Maria Eugenia Rojas"),
    ("rancheria", "Rancheria"),
    ("villa_laura", "Villa Laura"),
    ("urbanizacion_villa_armando", "Urbanizacion Villa Armando"),
    ("urbanizacion_bella_vista", "Urbanizacion Bella Vista"),
    ("urbanizacion_solmar", "Urbanizacion Solmar"),
    ("buenos_aires", "Buenos Aires"),
    ("los_cerezos", "Los Cerezos"),
    ("siete_de_agosto", "7 de Agosto"),
    ("urbanizacion_pareigua", "Urbanizacion Pareigua"),
    ("claudia_catalina", "Claudia Catalina"),
    ("pilar_del_rio", "Pilar del Rio"),
    ("urbanizacion_wuetapia", "Urbanizacion Wuetapia"),
    ("villa_comfamiliar", "Urbanizacion Villa Comfamiliar"),
    ("urbanizacion_villa_del_mar", "Urbanizacion Villa del Mar"),
    ("urbanizacion_villa_tatiana", "Urbanizacion Villa Tatiana"),
    ("villa_fatima", "Villa Fatima"),
    ("ciudadela_el_dividivi", "Ciudadela El Dividivi"),
    ("los_almendros", "Los Almendros"),
    ("los_loteros", "Los Loteros"),
    ("villa_sharin", "Villa Sharin"),
    ("urbanizacion_la_floresta", "Urbanizacion La Floresta"),
    ("hugo_zuniga", "Hugo Zuniga"),
    ("urbanizacion_san_judas_tadeo", "Urbanizacion San Judas Tadeo"),
    ("urbanizacion_san_isidro", "Urbanizacion San Isidro"),
    ("villa_yolima", "Villa Yolima"),
    ("villa_jardin", "Villa Jardin"),
    ("treinta_y_uno_de_octubre", "31 de Octubre"),
    ("urbanizacion_la_mano_de_dios", "Urbanizacion La Mano de Dios"),
    ("nuevo_milenio", "Nuevo Milenio"),
    ("urbanizacion_villa_aurora", "Urbanizacion Villa Aurora"),
    ("urbanizacion_taguaira", "Urbanizacion Taguaira"),
    ("la_lucha", "La Lucha"),
    ("la_luchita", "La Luchita"),
    ("la_provincia", "La Provincia"),
    ("fundacion_casa_del_abuelo", "Fundacion Casa del Abuelo"),
]

CITY_NEIGHBORHOODS = {
    "riohacha": {
        "label": "Riohacha",
        "barrios": RIOHACHA_BARRIOS,
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
    owner = models.ForeignKey(
        "users.AppUser",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_homes",
    )
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
