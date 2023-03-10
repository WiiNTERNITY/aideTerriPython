# Generated by Django 2.2.6 on 2019-11-04 10:59

import core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0080_auto_20191104_1028"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="subvention_rate",
            field=core.fields.PercentRangeField(
                blank=True,
                help_text="If this is a subvention aid, specify the rate.",
                null=True,
                verbose_name="Subvention rate, min. and max. (in round %)",
            ),
        ),
    ]
