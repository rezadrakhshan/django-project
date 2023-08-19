# Generated by Django 4.2.3 on 2023-07-07 12:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_remove_list_status_list_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='id',
        ),
        migrations.AddField(
            model_name='list',
            name='slug',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
