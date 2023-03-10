# Generated by Django 3.2.15 on 2022-09-27 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0030_user_acquisition_channel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="beneficiary_function",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mayor", "Maire"),
                    ("elected", "Élu"),
                    ("town_clerk", "Secrétaire de mairie"),
                    ("agent", "Agent territorial"),
                    ("other", "Autre"),
                ],
                max_length=32,
                null=True,
                verbose_name="Fonction du bénéficiaire",
            ),
        ),
    ]
