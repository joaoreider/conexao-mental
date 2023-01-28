# Generated by Django 4.1.5 on 2023-01-28 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contato",
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
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("telefone", models.CharField(max_length=255)),
                (
                    "Usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuario.usuario",
                    ),
                ),
            ],
        ),
    ]
