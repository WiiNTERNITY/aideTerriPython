# Generated by Django 3.1.7 on 2021-02-23 14:28

from django.db import migrations
from django.db.migrations.operations.special import RunPython
from core.utils import reupload_files


class Migration(migrations.Migration):

    dependencies = [
        ("programs", "0006_program_logo"),
    ]

    operations = [RunPython(reupload_files("programs.Program", "logo"), RunPython.noop)]
