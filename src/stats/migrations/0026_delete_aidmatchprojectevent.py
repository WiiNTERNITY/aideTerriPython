# Generated by Django 3.2.6 on 2021-08-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0025_auto_20210806_1540"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AidMatchProjectEvent",
        ),
    ]