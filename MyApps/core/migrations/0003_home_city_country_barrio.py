from django.db import migrations, models


CITY_MAP = {
    "riohacha": "riohacha",
    "maicao": "maicao",
    "barranquilla": "barranquilla",
    "bogota": "bogota",
    "bogotá": "bogota",
    "medellin": "medellin",
    "medellín": "medellin",
}


def normalize_homes(apps, schema_editor):
    Home = apps.get_model("core", "Home")

    for home in Home.objects.all():
        city = (home.city or "").strip().lower()
        home.city = CITY_MAP.get(city, "riohacha")
        home.country = "Colombia"
        home.barrio = home.barrio or "centro"
        home.save(update_fields=["city", "country", "barrio"])


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="home",
            name="barrio",
            field=models.CharField(default="centro", max_length=100),
        ),
        migrations.AlterField(
            model_name="home",
            name="city",
            field=models.CharField(
                choices=[
                    ("riohacha", "Riohacha"),
                    ("maicao", "Maicao"),
                    ("barranquilla", "Barranquilla"),
                    ("bogota", "Bogota"),
                    ("medellin", "Medellin"),
                ],
                default="riohacha",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="home",
            name="country",
            field=models.CharField(default="Colombia", editable=False, max_length=100),
        ),
        migrations.RunPython(normalize_homes, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="home",
            name="barrio",
            field=models.CharField(
                choices=[
                    ("centro", "Centro"),
                    ("los_olivos", "Los Olivos"),
                    ("cooperativo", "Cooperativo"),
                    ("marbella", "Marbella"),
                    ("villa_comfamiliar", "Villa Comfamiliar"),
                    ("san_francisco", "San Francisco"),
                    ("la_floresta", "La Floresta"),
                    ("el_carmen", "El Carmen"),
                    ("villa_amelia", "Villa Amelia"),
                    ("el_prado", "El Prado"),
                    ("alto_prado", "Alto Prado"),
                    ("riomar", "Riomar"),
                    ("boston", "Boston"),
                    ("ciudad_jardin", "Ciudad Jardin"),
                    ("chapinero", "Chapinero"),
                    ("usaquen", "Usaquen"),
                    ("suba", "Suba"),
                    ("teusaquillo", "Teusaquillo"),
                    ("kennedy", "Kennedy"),
                    ("el_poblado", "El Poblado"),
                    ("laureles", "Laureles"),
                    ("belen", "Belen"),
                    ("robledo", "Robledo"),
                    ("guayabal", "Guayabal"),
                ],
                default="centro",
                max_length=100,
            ),
        ),
    ]
