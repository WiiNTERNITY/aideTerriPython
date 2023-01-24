# Generated by Django 2.2.1 on 2019-09-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="description",
            field=models.TextField(default="", verbose_name="Description"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="program",
            name="short_description",
            field=models.CharField(
                default="",
                help_text="Will only appear in search results. 300 chars. max.",
                max_length=300,
                verbose_name="Short description",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="program",
            name="slug",
            field=models.SlugField(default="", verbose_name="Slug"),
            preserve_default=False,
        ),
    ]
