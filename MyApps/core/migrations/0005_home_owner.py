import django.db.models.deletion
from django.db import migrations, models


def copy_owner_from_user_home(apps, schema_editor):
    Home = apps.get_model("core", "Home")
    AppUser = apps.get_model("users", "AppUser")

    for home in Home.objects.all():
        owner = AppUser.objects.filter(home_id=home.id).order_by("id").first()

        if owner:
            home.owner_id = owner.id
            home.save(update_fields=["owner"])


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
        ("core", "0004_alter_home_barrio"),
    ]

    operations = [
        migrations.AddField(
            model_name="home",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="owned_homes",
                to="users.appuser",
            ),
        ),
        migrations.RunPython(copy_owner_from_user_home, migrations.RunPython.noop),
    ]
