# Generated by Django 2.1.2 on 2018-12-10 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0050_aid_is_imported"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="import_uniqueid",
            field=models.CharField(
                blank=True,
                max_length=20,
                verbose_name="Unique identifier for imported data",
            ),
        ),
        migrations.AlterField(
            model_name="aid",
            name="is_imported",
            field=models.BooleanField(default=False, verbose_name="Is imported?"),
        ),
    ]
