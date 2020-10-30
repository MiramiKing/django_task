# Generated by Django 3.1 on 2020-10-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20201015_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristics',
            options={'verbose_name': 'Характеристики', 'verbose_name_plural': 'Характеристики'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='category',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='design',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='gendertype',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='image',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='nomenset',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='product',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='set',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='set',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Торговое предложение'),
        ),
        migrations.AlterField(
            model_name='size',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
        migrations.AlterField(
            model_name='typemodel',
            name='guid',
            field=models.CharField(max_length=100, verbose_name='guid'),
        ),
    ]
