from django.db import migrations, models


def populate_usernames(apps, schema_editor):
    AppUser = apps.get_model("users", "AppUser")

    for user in AppUser.objects.all():
        if user.username:
            continue

        base = ""

        if user.email:
            base = user.email.split("@")[0]

        if not base:
            base = f"user{user.pk}"

        base = base[:140]
        username = base
        counter = 1

        while AppUser.objects.filter(username=username).exclude(pk=user.pk).exists():
            suffix = f"-{counter}"
            username = f"{base[:150 - len(suffix)]}{suffix}"
            counter += 1

        user.username = username
        user.save(update_fields=["username"])


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appuser",
            name="username",
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
        migrations.RunPython(populate_usernames, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="appuser",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
