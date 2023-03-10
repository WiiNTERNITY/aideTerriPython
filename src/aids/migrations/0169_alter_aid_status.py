# Generated by Django 3.2.16 on 2022-11-10 13:21

from django.db import migrations
import django_xworkflows.models


class Migration(migrations.Migration):

    dependencies = [
        ('aids', '0168_aidproject_add_aid_informations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aid',
            name='status',
            field=django_xworkflows.models.StateField(max_length=16, verbose_name='Statut', workflow=django_xworkflows.models._SerializedWorkflow(initial_state='draft', name='AidWorkflow', states=['draft', 'reviewable', 'published', 'deleted', 'merged'])),
        ),
    ]
