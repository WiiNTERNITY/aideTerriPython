# Generated by Django 2.2.5 on 2019-11-04 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0079_remove_aid_subvention_rate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="aid",
            old_name="subvention_rate_range",
            new_name="subvention_rate",
        ),
    ]
