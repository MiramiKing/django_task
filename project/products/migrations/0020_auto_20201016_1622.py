# Generated by Django 3.1 on 2020-10-16 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20201016_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='is_mainphoto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.image', verbose_name='Фотография'),
        ),
    ]
