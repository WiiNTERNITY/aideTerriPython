# Generated by Django 3.2.16 on 2022-11-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0013_public_projects_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="budget",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Budget prévisionnel"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="other_project_owner",
            field=models.CharField(
                blank=True,
                max_length=180,
                null=True,
                verbose_name="Autre maître d'ouvrage",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="step",
            field=models.CharField(
                blank=True,
                choices=[
                    ("considered", "En réflexion"),
                    ("ongoing", "En cours"),
                    ("finished", "Réalisé"),
                ],
                max_length=10,
                null=True,
                verbose_name="Avancement du projet",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="due_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Date d'échéance"
            ),
        ),
    ]
