# Generated by Django 2.2.9 on 2020-02-17 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0003_set_slugs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(verbose_name="Slug"),
        ),
        migrations.AlterField(
            model_name="theme",
            name="slug",
            field=models.SlugField(verbose_name="Slug"),
        ),
    ]
