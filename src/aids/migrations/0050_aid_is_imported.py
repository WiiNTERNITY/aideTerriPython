# Generated by Django 2.1.2 on 2018-12-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0049_auto_20181115_1606"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="is_imported",
            field=models.BooleanField(
                default=False, verbose_name="Is imported from a third-party?"
            ),
        ),
    ]
