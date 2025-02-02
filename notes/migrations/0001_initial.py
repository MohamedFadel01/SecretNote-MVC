# Generated by Django 5.1.1 on 2024-10-09 08:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SecretNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                (
                    "url_key",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("expiration_time", models.DateTimeField(blank=True, null=True)),
                ("max_views", models.IntegerField(default=1)),
                ("views", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
