# Generated by Django 2.0 on 2019-09-24 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20190924_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag_set',
        ),
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', to='article.Article'),
        ),
    ]
