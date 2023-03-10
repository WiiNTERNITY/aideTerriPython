# Generated by Django 3.2.12 on 2022-03-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geofr", "0035_auto_20220224_1828"),
    ]

    operations = [
        migrations.AddField(
            model_name="perimeter",
            name="categories_count",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="nombre de catégories"
            ),
        ),
        migrations.AddField(
            model_name="perimeter",
            name="live_aids_count",
            field=models.PositiveSmallIntegerField(
                blank=True, null=True, verbose_name="nombre d’aides live"
            ),
        ),
    ]
