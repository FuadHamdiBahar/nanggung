# Generated by Django 3.0.4 on 2020-06-17 03:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200617_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='deskripsi',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produk',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='produk',
            name='foto',
            field=models.ImageField(upload_to='upload'),
        ),
    ]