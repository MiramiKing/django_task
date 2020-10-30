# Generated by Django 3.1 on 2020-10-16 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_auto_20201016_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteristics',
            name='gender_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.gendertype', verbose_name='Половая принадлежность'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer', verbose_name='Производитель'),
        ),
    ]
