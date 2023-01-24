# Generated by Django 3.2.12 on 2022-03-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0022_userlastconnexion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="contributor_organization",
            field=models.CharField(
                blank=True, max_length=128, verbose_name="Organisme (ancien champ)"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="contributor_role",
            field=models.CharField(
                blank=True, max_length=128, verbose_name="Rôle (ancien champ)"
            ),
        ),
    ]