# Generated by Django 2.1.1 on 2018-10-02 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0036_set_slugs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="slug",
            field=models.SlugField(
                blank=True,
                default="",
                help_text="Let it empty so it will be autopopulated.",
                verbose_name="Slug",
            ),
            preserve_default=False,
        ),
    ]
