# Generated by Django 4.1.3 on 2022-11-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_rename_nick_name_user_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="belong",
        ),
        migrations.AddField(
            model_name="user",
            name="belongs",
            field=models.ManyToManyField(to="users.club"),
        ),
    ]
