# Generated by Django 2.2.6 on 2019-10-29 13:44

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0074_update_technical_aid_values"),
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
                        ("technical", "Technical"),
                        ("financial", "Financial"),
                        ("legal", "Legal"),
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
    ]
