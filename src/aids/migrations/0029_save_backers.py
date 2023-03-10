# Generated by Django 2.1.1 on 2018-09-20 12:34

from django.db import migrations


def save_backers(apps, schema_editor):
    Aid = apps.get_model("aids", "Aid")
    aids = Aid.objects.all()
    for aid in aids:
        aid.backers.add(aid.backer)
        aid.save()


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0028_aid_backers"),
    ]

    operations = [
        migrations.RunPython(save_backers),
    ]
