# Generated by Django 3.1 on 2020-10-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20201016_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='characteristics',
            name='composition',
            field=models.TextField(default='', verbose_name='Сравнение'),
            preserve_default=False,
        ),
    ]
