# Generated by Django 3.2.2 on 2021-05-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20210510_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='screenshot1',
            field=models.ImageField(default=0, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenshot2',
            field=models.ImageField(default=0, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenshot3',
            field=models.ImageField(default=0, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenshot4',
            field=models.ImageField(default=0, upload_to='uploads/'),
        ),
    ]