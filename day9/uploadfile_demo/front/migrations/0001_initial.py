# Generated by Django 2.0 on 2019-09-30 02:37

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
                ('thumbnail', models.FileField(upload_to='files', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'gif'], message='必须是图片类型的文件')])),
            ],
        ),
    ]
