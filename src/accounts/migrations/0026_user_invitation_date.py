# Generated by Django 3.2.12 on 2022-05-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0025_user_invitation_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="invitation_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Date de l'invitation"
            ),
        ),
    ]