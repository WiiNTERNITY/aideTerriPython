# Generated by Django 2.2.9 on 2020-03-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0102_auto_20200302_1041"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="project_examples",
            field=models.TextField(
                blank=True, default="", verbose_name="Project examples"
            ),
        ),
    ]