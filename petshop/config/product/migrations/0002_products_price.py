# Generated by Django 4.2.5 on 2023-11-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]