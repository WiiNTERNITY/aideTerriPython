# Generated by Django 2.1.1 on 2018-09-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backers", "0001_initial"),
        ("aids", "0027_auto_20180918_1047"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="backers",
            field=models.ManyToManyField(
                related_name="aids", to="backers.Backer", verbose_name="Backers"
            ),
        ),
    ]
