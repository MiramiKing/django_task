# Generated by Django 3.1 on 2020-10-23 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0053_auto_20201023_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characteristics',
            old_name='brand',
            new_name='brands',
        ),
    ]
