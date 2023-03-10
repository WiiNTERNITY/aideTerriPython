# Generated by Django 3.2.6 on 2021-04-25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("keywords", "0001_initial"),
        ("aids", "0156_search_vector_fields_range"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="keywords",
            field=models.ManyToManyField(
                related_name="aids",
                to="keywords.Keyword",
                blank=True,
                verbose_name="Mots clé",
            ),
        ),
    ]
