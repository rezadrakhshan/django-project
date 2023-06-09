# Generated by Django 4.1.7 on 2023-06-02 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Year_of_construction',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=11, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
