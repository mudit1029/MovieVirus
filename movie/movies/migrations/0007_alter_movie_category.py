# Generated by Django 3.2.2 on 2021-05-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20210509_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('B', 'Bollywood'), ('H', 'Hollywood'), ('A', 'Animated'), ('S', 'South'), ('W', 'Web Series')], max_length=1),
        ),
    ]
