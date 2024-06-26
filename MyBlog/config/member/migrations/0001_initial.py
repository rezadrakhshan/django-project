# Generated by Django 5.0.1 on 2024-03-15 13:40

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'کد',
                'verbose_name_plural': 'کد ها',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='نام')),
                ('last_name', models.CharField(max_length=50, verbose_name=' نام خانوداگی')),
                ('user_name', models.CharField(max_length=50, verbose_name='نام کاربری')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('amount', models.BigIntegerField(default=0, verbose_name='اعتبار')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'پروفایل',
                'verbose_name_plural': 'پروفایل ها',
            },
        ),
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='member.profile', verbose_name='دنبال کننده')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.profile', verbose_name='دنبال شونده')),
            ],
            options={
                'verbose_name': 'دنبال کننده ',
                'verbose_name_plural': 'دنبال کنندگان',
            },
        ),
        migrations.CreateModel(
            name='SuperAccount',
            fields=[
                ('super_account', models.CharField(choices=[('G', 'طلایی'), ('D', 'الماسی'), ('S', 'نقره ای')], max_length=50, verbose_name='نوع اکانت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در')),
                ('slug', models.SlugField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.profile', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'حساب',
                'verbose_name_plural': 'حساب ها',
            },
        ),
    ]
