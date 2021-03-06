# Generated by Django 3.2.11 on 2022-01-28 16:26

from typing import List, Tuple

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[Tuple] = []

    operations = [
        migrations.CreateModel(
            name="Dislike",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Dislike",
                "verbose_name_plural": "Dislikes",
            },
        ),
        migrations.CreateModel(
            name="Like",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Like",
                "verbose_name_plural": "Likes",
            },
        ),
    ]
