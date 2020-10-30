# Generated by Django 3.1 on 2020-10-30 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0055_auto_20201026_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('region_code', models.CharField(max_length=100, verbose_name='Регион')),
                ('code', models.SmallIntegerField(verbose_name='Код города')),
                ('sub_region', models.SmallIntegerField(verbose_name='Код региона')),
            ],
            options={
                'verbose_name': 'Города',
                'verbose_name_plural': 'Города',
            },
        ),
    ]
