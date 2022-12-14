# Generated by Django 4.1.2 on 2022-12-09 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Works",
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
                ("file_name", models.CharField(help_text="Name", max_length=50)),
                ("image", models.ImageField(help_text="Image", upload_to="bx/media")),
                (
                    "service_type",
                    models.CharField(
                        choices=[
                            ("Logo", "logo"),
                            ("Graphic Design", "graphics"),
                            ("Info Graphics", "info"),
                        ],
                        default=1,
                        help_text="Service Type",
                        max_length=50,
                    ),
                ),
                (
                    "date_uploaded",
                    models.DateField(
                        blank=True,
                        default=datetime.datetime.now,
                        help_text="Date uploaded",
                    ),
                ),
            ],
        ),
    ]
