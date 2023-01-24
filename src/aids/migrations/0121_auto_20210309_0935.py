# Generated by Django 3.1.7 on 2021-03-09 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("aids", "0120_merge_20210222_0957"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="author",
            field=models.ForeignKey(
                help_text="Who is submitting the aid?",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="aids",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
    ]