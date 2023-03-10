# Generated by Django 3.2 on 2021-04-27 14:35

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0017_aideligibilitytestevent"),
    ]

    operations = [
        migrations.AddField(
            model_name="aidviewevent",
            name="targeted_audiences",
            field=core.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("commune", "Communes"),
                        ("epci", "Audience EPCI"),
                        ("department", "Departments"),
                        ("region", "Regions"),
                        ("association", "Associations"),
                        ("private_sector", "Private sector"),
                        ("public_cies", "Local public companies"),
                        ("public_org", "Public organization"),
                        ("researcher", "Research"),
                        ("private_person", "Individuals"),
                        ("farmer", "Farmers"),
                    ],
                    max_length=32,
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="Targeted audiences",
            ),
        ),
    ]
