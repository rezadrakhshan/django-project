# Generated by Django 4.1.7 on 2023-06-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0017_remove_movie_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='company',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
