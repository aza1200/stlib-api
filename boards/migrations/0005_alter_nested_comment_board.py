# Generated by Django 4.1.3 on 2022-12-01 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("boards", "0004_board_like_users_alter_comment_board_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nested_comment",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nested_comments",
                to="boards.board",
            ),
        ),
    ]
