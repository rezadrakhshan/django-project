# Generated by Django 5.0.6 on 2024-07-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_coupon_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ManyToManyField(related_name='coupon', to='shop.coupon'),
        ),
    ]
