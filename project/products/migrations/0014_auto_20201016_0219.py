# Generated by Django 3.1 on 2020-10-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
    ]
