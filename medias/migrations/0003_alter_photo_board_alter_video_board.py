# Generated by Django 4.1.3 on 2022-12-05 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0006_alter_nested_comment_comment"),
        ("medias", "0002_alter_photo_file_alter_video_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="board",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="boards.board",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="board",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="videos",
                to="boards.board",
            ),
        ),
    ]
