# Generated by Django 3.2.2 on 2021-05-10 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20210510_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='screenshot1',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenshot2',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenshot3',
            field=models.ImageField(upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenshot4',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
