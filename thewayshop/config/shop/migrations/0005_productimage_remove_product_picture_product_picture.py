# Generated by Django 5.0.6 on 2024-05-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ManyToManyField(related_name='pic', to='shop.productimage'),
        ),
    ]