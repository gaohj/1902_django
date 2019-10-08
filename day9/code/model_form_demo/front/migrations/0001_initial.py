# Generated by Django 2.0 on 2019-09-29 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('word_num', models.IntegerField()),
                ('price', models.FloatField(validators=[django.core.validators.MaxValueValidator(limit_value=100)])),
            ],
        ),
    ]
