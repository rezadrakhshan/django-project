# Generated by Django 4.1.7 on 2023-06-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_alter_movie_imdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_link',
            field=models.URLField(max_length=400),
        ),
    ]
