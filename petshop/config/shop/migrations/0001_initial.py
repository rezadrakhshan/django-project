# Generated by Django 4.2.5 on 2023-10-01 19:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('slug', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
    ]
