# Generated by Django 3.2.11 on 2022-03-09 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0003_comment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
