# Generated by Django 2.2.5 on 2019-11-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backers", "0003_backer_is_corporate"),
        ("aids", "0089_auto_20191121_1137"),
    ]

    operations = [
        migrations.RenameField(
            model_name="aid",
            old_name="backers",
            new_name="financers",
        ),
    ]