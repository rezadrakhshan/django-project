# Generated by Django 4.2.7 on 2023-11-24 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='table',
            options={'ordering': ['place']},
        ),
        migrations.RemoveField(
            model_name='table',
            name='point',
        ),
    ]
