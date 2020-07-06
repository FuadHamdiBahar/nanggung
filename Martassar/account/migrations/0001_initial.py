# Generated by Django 3.0.4 on 2020-07-06 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('0', 'Laki-Laki'), ('1', 'Perempuan')], max_length=20)),
            ],
        ),
    ]
