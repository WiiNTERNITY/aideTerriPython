# Generated by Django 2.1.2 on 2018-10-19 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("aids", "0038_auto_20181009_1451"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aid",
            name="author",
            field=models.ForeignKey(
                default=1,
                help_text="Who is submitting the aid?",
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
            preserve_default=False,
        ),
    ]
