# Generated by Django 3.1 on 2020-10-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_set_composition'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='maintenance',
            field=models.TextField(null=True, verbose_name='Уход за товаром'),
        ),
    ]
