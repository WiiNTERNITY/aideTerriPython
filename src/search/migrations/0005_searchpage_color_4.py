# Generated by Django 2.2.13 on 2020-06-08 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0004_auto_20200608_1011"),
    ]

    operations = [
        migrations.AddField(
            model_name="searchpage",
            name="color_4",
            field=models.CharField(
                blank=True,
                help_text="Link colors",
                max_length=10,
                verbose_name="Color 4",
            ),
        ),
    ]
