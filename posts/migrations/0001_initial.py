# Generated by Django 3.2.11 on 2022-01-28 16:26

from typing import List, Tuple

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[Tuple] = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("photo", models.ImageField(upload_to="")),
                ("description", models.TextField(blank=True, max_length=500)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Post",
                "verbose_name_plural": "Posts",
            },
        ),
    ]
