# Generated by Django 2.2.17 on 2021-01-20 19:19

from django.db import migrations


def init_is_visible_to_users_field(apps, schema_editor):
    """
    Set is_visible_to_users to False for manually_created Perimeters
    """
    Perimeter = apps.get_model("geofr", "Perimeter")
    perimeters = Perimeter.objects.all()
    for perimeter in perimeters:
        if perimeter.manually_created:
            perimeter.is_visible_to_users = False
            perimeter.save()


class Migration(migrations.Migration):

    dependencies = [
        ("geofr", "0029_perimeter_is_visible_to_users"),
    ]

    operations = [migrations.RunPython(init_is_visible_to_users_field)]
