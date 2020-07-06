# Generated by Django 3.0.4 on 2020-06-17 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_keranjang_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='keranjang',
            name='success_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='keranjang',
            name='success',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='keranjang',
            name='transaction_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
