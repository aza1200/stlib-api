# Generated by Django 4.1.3 on 2022-11-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="nick_name",
            new_name="name",
        ),
    ]
