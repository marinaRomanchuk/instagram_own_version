# Generated by Django 3.2.11 on 2022-02-23 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0003_alter_post_photo"),
        ("likes", "0005_auto_20220223_1539"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikeDislike",
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
                ("is_like", models.BooleanField(default=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "LikeDislike",
                "verbose_name_plural": "LikesDislikes",
            },
        ),
    ]