# Generated by Django 2.2.17 on 2021-01-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0021_searchpage_show_aid_type_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="searchpage",
            name="date_updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Date updated"),
        ),
    ]
