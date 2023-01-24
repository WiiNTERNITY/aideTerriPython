# Generated by Django 3.2.12 on 2022-04-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0155_create_import_raw_object_temp"),
        ("search", "0037_alter_searchpage_available_audiences"),
    ]

    operations = [
        migrations.AlterField(
            model_name="searchpage",
            name="highlighted_aids",
            field=models.ManyToManyField(
                blank=True,
                help_text="Il est possible de mettre jusqu'à 9 aides en avant.              Les aides mises en avant s'affichent en haut des résultats du portail,              et n’ont pas de mise en forme particulière.",
                related_name="highlighted_in_search_pages",
                to="aids.Aid",
                verbose_name="Highlighted aids",
            ),
        ),
    ]