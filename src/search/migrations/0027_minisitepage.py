# Generated by Django 3.2.4 on 2021-06-08 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_alter_page_minisite"),
        ("search", "0026_searchpage_administrators"),
    ]

    operations = [
        migrations.CreateModel(
            name="MinisitePage",
            fields=[],
            options={
                "verbose_name": "Page",
                "verbose_name_plural": "Pages",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("pages.page",),
        ),
    ]