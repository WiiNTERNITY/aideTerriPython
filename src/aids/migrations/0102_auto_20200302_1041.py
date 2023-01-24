# Generated by Django 2.2.9 on 2020-03-02 09:41

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0101_auto_20200210_1115"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="aid_types",
            field=core.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("grant", "Grant"),
                        ("loan", "Loan"),
                        ("recoverable_advance", "Recoverable advance"),
                        ("technical", "Technical engineering"),
                        ("financial", "Financial engineering"),
                        ("legal", "Legal engineering"),
                        ("other", "Other"),
                    ],
                    max_length=32,
                ),
                blank=True,
                help_text="Specify the aid type or types.",
                null=True,
                size=None,
                verbose_name="Aid types",
            ),
        ),
        migrations.AlterField(
            model_name="aid",
            name="start_date",
            field=models.DateField(
                blank=True,
                help_text="When is the application opening?",
                null=True,
                verbose_name="Start date",
            ),
        ),
    ]
