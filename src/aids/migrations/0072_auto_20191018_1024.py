# Generated by Django 2.2.2 on 2019-10-18 08:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0071_auto_20191010_0947"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="tags",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=50),
                blank=True,
                default=list,
                size=30,
                verbose_name="Tags",
            ),
        ),
    ]
