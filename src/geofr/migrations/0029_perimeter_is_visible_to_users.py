# Generated by Django 2.2.17 on 2021-01-20 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geofr", "0028_auto_20200616_1117"),
    ]

    operations = [
        migrations.AddField(
            model_name="perimeter",
            name="is_visible_to_users",
            field=models.BooleanField(
                default=True, verbose_name="The perimeter is visible to users"
            ),
        ),
    ]
