# Generated by Django 3.2.2 on 2021-05-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('poster', models.CharField(max_length=300)),
                ('imdbID', models.CharField(max_length=300)),
                ('api', models.CharField(max_length=300)),
            ],
        ),
    ]
