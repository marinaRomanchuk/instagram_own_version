# Generated by Django 3.2.11 on 2022-02-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="photo",
            field=models.ImageField(upload_to="post"),
        ),
    ]
