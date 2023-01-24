# Generated by Django 3.2 on 2021-04-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eligibility", "0003_eligibilitytestquestion"),
    ]

    operations = [
        migrations.AddField(
            model_name="eligibilitytest",
            name="conclusion_failure",
            field=models.TextField(
                blank=True, verbose_name="Une conclusion si le test est négatif"
            ),
        ),
        migrations.AddField(
            model_name="eligibilitytest",
            name="conclusion_success",
            field=models.TextField(
                blank=True, verbose_name="Une conclusion si le test est positif"
            ),
        ),
        migrations.AlterField(
            model_name="eligibilitytest",
            name="conclusion",
            field=models.TextField(blank=True, verbose_name="Une conclusion générale"),
        ),
    ]