# Generated by Django 4.1.7 on 2023-07-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialplatform', '0007_followerscount'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
