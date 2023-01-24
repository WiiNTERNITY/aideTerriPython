# Generated by Django 2.2.5 on 2019-11-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backers", "0003_backer_is_corporate"),
        ("aids", "0090_auto_20191125_1526"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="instructors",
            field=models.ManyToManyField(
                related_name="instructors_aids",
                to="backers.Backer",
                verbose_name="Instructors",
            ),
        ),
        migrations.AlterField(
            model_name="aid",
            name="financers",
            field=models.ManyToManyField(
                related_name="financers_aids",
                to="backers.Backer",
                verbose_name="Financers",
            ),
        ),
    ]