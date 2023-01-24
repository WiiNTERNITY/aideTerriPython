# Generated by Django 2.2.17 on 2020-12-03 12:03

import backers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backers", "0006_add_slug_help_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="backer",
            name="external_link",
            field=models.URLField(
                blank=True,
                help_text="The url for the backer's website",
                null=True,
                verbose_name="External link",
            ),
        ),
        migrations.AddField(
            model_name="backer",
            name="is_spotlighted",
            field=models.BooleanField(
                default=False,
                help_text="If the backer is spotlighted, its logo appears in the HomePage",
                verbose_name="Is a spotlighted backer?",
            ),
        ),
        migrations.AddField(
            model_name="backer",
            name="logo",
            field=models.FileField(
                blank=True,
                help_text="Make sure the file is not too heavy. Prefer svg files.",
                null=True,
                upload_to=backers.models.logo_upload_to,
                verbose_name="Logo image",
            ),
        ),
    ]