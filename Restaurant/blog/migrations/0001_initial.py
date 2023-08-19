# Generated by Django 4.1.7 on 2023-03-24 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='blog_photos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('upadated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('p', 'punlished'), ('d', 'draft')], max_length=1)),
            ],
        ),
    ]
