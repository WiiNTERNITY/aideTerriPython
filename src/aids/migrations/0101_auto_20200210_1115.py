# Generated by Django 2.2.9 on 2020-02-10 10:15

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0100_auto_20200203_1433"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="perimeter_suggestion",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name="Perimeter suggestion",
            ),
        ),
    ]
