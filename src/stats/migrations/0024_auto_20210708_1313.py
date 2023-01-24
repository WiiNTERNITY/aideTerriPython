# Generated by Django 3.2.4 on 2021-07-08 11:13

import core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stats", "0023_cleanup_choices_translations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aidsearchevent",
            name="targeted_audiences",
            field=core.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("commune", "Communes"),
                        ("epci", "EPCI à fiscalité propre"),
                        ("department", "Départements"),
                        ("region", "Régions"),
                        ("special", "Collectivités d'outre-mer à statuts particuliers"),
                        ("association", "Associations"),
                        ("private_sector", "Entreprises privées"),
                        (
                            "public_cies",
                            "Entreprises publiques locales (Sem, Spl, SemOp)",
                        ),
                        (
                            "public_org",
                            "Établissements publics (écoles, bibliothèques…) / Services de l'État",
                        ),
                        ("researcher", "Recherche"),
                        ("private_person", "Particuliers"),
                        ("farmer", "Agriculteurs"),
                    ],
                    max_length=32,
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="Targeted audiences",
            ),
        ),
        migrations.AlterField(
            model_name="aidviewevent",
            name="targeted_audiences",
            field=core.fields.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("commune", "Communes"),
                        ("epci", "EPCI à fiscalité propre"),
                        ("department", "Départements"),
                        ("region", "Régions"),
                        ("special", "Collectivités d'outre-mer à statuts particuliers"),
                        ("association", "Associations"),
                        ("private_sector", "Entreprises privées"),
                        (
                            "public_cies",
                            "Entreprises publiques locales (Sem, Spl, SemOp)",
                        ),
                        (
                            "public_org",
                            "Établissements publics (écoles, bibliothèques…) / Services de l'État",
                        ),
                        ("researcher", "Recherche"),
                        ("private_person", "Particuliers"),
                        ("farmer", "Agriculteurs"),
                    ],
                    max_length=32,
                ),
                blank=True,
                null=True,
                size=None,
                verbose_name="Targeted audiences",
            ),
        ),
    ]
