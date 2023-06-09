# Generated by Django 4.1.7 on 2023-06-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('imdb', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('c', 'coming soon'), ('p', 'Published')], default='Available', max_length=100)),
                ('img', models.ImageField(null=True, upload_to='news_photos')),
                ('imdb_link', models.CharField(max_length=100)),
            ],
        ),
    ]
