# Generated by Django 4.1.7 on 2023-06-19 09:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_company_movie_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('slug', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='news_photos')),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
        ),
    ]
