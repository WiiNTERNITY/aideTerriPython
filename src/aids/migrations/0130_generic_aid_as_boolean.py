# Generated by Django 3.1.8 on 2021-05-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0129_auto_20210413_1118"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="is_generic",
            field=models.BooleanField(default=False, verbose_name="Is generic aid"),
        ),
    ]
