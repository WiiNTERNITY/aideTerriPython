# Generated by Django 3.2.6 on 2022-01-31 09:25

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0020_alter_user_beneficiary_function"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.FileField(
                blank=True,
                help_text="Assurez vous que l'image n'est pas trop lourde.",
                null=True,
                upload_to=accounts.models.logo_upload_to,
                verbose_name="Avatar de l'utilisateur",
            ),
        ),
    ]