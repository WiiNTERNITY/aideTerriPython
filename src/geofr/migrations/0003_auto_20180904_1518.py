# Generated by Django 2.1.1 on 2018-09-04 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geofr", "0002_remove_perimeter_country"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="perimeter",
            unique_together={("scale", "code")},
        ),
    ]
