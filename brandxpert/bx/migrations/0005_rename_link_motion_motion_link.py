# Generated by Django 4.1.2 on 2022-12-12 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bx", "0004_alter_motion_link"),
    ]

    operations = [
        migrations.RenameField(
            model_name="motion",
            old_name="link",
            new_name="motion_link",
        ),
    ]
