# Generated by Django 3.1 on 2020-08-18 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20200815_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Rating star', 'verbose_name_plural': 'Rating stars'},
        ),
    ]
