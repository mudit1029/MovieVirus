# Generated by Django 3.2.2 on 2021-05-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20210510_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='screenshot1Name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenshot2Name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenshot3Name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='screenshot4Name',
            field=models.CharField(default='', max_length=300),
        ),
    ]