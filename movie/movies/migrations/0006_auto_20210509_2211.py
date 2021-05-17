# Generated by Django 3.2.2 on 2021-05-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movie_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('B', 'Bollywood'), ('H', 'Hollywood'), ('A', 'Animated')], default='B', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='dualAudio',
            field=models.BooleanField(default=False),
        ),
    ]
