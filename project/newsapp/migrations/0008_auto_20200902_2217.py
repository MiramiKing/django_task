# Generated by Django 3.1 on 2020-09-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0007_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='news',
        ),
        migrations.AddField(
            model_name='article',
            name='news',
            field=models.ManyToManyField(to='newsapp.News'),
        ),
    ]