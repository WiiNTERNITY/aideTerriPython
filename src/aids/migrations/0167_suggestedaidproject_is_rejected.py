# Generated by Django 3.2.15 on 2022-10-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0166_suggestedaidproject_is_associated"),
    ]

    operations = [
        migrations.AddField(
            model_name="suggestedaidproject",
            name="date_rejected",
            field=models.DateTimeField(
                blank=True,
                help_text="Date à laquelle cette aide a été rejetée par le porteur du projet",
                null=True,
                verbose_name="Date de rejet",
            ),
        ),
        migrations.AddField(
            model_name="suggestedaidproject",
            name="is_rejected",
            field=models.BooleanField(
                default=False,
                help_text="Cette aide a-t-elle été rejetée par le porteur du projet ?",
                verbose_name="Aide rejetée ?",
            ),
        ),
    ]
