# Generated by Django 2.1.1 on 2018-09-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geofr", "0007_perimeter_is_overseas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perimeter",
            name="is_overseas",
            field=models.BooleanField(null=True, verbose_name="Is overseas?"),
        ),
    ]
