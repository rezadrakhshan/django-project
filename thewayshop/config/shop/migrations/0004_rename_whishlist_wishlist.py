# Generated by Django 5.0.6 on 2024-05-30 06:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_whishlist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WhishList',
            new_name='WishList',
        ),
    ]
