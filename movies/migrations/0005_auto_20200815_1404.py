# Generated by Django 3.1 on 2020-08-15 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0004_auto_20200815_0434"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie", old_name="fees_in_usa", new_name="fees_in_use",
        ),
    ]