# Generated by Django 3.1.6 on 2021-02-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0117_auto_20201211_1520"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="application_url",
            field=models.URLField(
                blank=True, max_length=500, verbose_name="Application url"
            ),
        ),
        migrations.AlterField(
            model_name="aid",
            name="origin_url",
            field=models.URLField(
                blank=True, max_length=500, verbose_name="Origin URL"
            ),
        ),
    ]
