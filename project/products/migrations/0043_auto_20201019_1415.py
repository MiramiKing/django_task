# Generated by Django 3.1 on 2020-10-19 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0042_auto_20201019_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Категория'),
        ),
    ]
