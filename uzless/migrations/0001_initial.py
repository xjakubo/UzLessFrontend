# Generated by Django 3.2.23 on 2024-01-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrinterModel",
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
                ("printerId", models.IntegerField()),
                ("name", models.CharField(max_length=255)),
                ("printerTypeId", models.IntegerField()),
                ("printerQueueId", models.IntegerField()),
                ("printStateId", models.IntegerField()),
            ],
        ),
    ]
