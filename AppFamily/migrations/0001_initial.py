# Generated by Django 4.1 on 2022-08-23 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="familia",
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
                ("nombre", models.CharField(max_length=50)),
                ("apellido", models.CharField(max_length=50)),
                ("apePaterno", models.CharField(max_length=70)),
                ("fechaNacimiento", models.CharField(max_length=70)),
                ("telefono", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
