# Generated by Django 3.2.2 on 2021-05-10 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20210510_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='screenshot1Name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='screenshot2Name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='screenshot3Name',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='screenshot4Name',
        ),
    ]
