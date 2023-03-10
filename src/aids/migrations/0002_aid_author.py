# Generated by Django 2.1 on 2018-08-14 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("aids", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="aid",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
            preserve_default=False,
        ),
    ]
