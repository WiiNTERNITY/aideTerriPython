# Generated by Django 3.1.7 on 2021-03-05 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("programs", "0007_reupload_files"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="date_created",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Date created"
            ),
        ),
    ]
