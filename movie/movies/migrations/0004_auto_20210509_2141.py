# Generated by Django 3.2.2 on 2021-05-09 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='directors',
        ),
    ]
