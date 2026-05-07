from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_home_owner"),
        ("users", "0002_appuser_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appuser",
            name="home",
        ),
    ]
