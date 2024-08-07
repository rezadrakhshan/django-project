# Generated by Django 5.0.6 on 2024-07-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_cart_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('P', 'Paid'), ('U', 'Unpaid')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
