# Generated by Django 2.1.1 on 2018-10-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0034_auto_20180928_1556"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="slug",
            field=models.SlugField(blank=True, null=True, verbose_name="Slug"),
        ),
    ]
