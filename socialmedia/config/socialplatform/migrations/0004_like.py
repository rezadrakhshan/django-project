# Generated by Django 4.2.1 on 2023-06-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialplatform', '0003_rename_user_post_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=90)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
