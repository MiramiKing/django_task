# Generated by Django 3.1 on 2020-10-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0046_auto_20201019_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.brands', verbose_name='Бренд'),
        ),
    ]