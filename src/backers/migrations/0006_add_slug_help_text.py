# Generated by Django 2.2.16 on 2020-10-06 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backers", "0005_set_backers_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backer",
            name="slug",
            field=models.SlugField(
                help_text="Slug field is set when creating the backer and can not be changed after.",
                verbose_name="Slug",
            ),
        ),
    ]
