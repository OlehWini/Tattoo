# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20161017_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sur_name', models.CharField(max_length=100)),
                ('years_old', models.IntegerField()),
                ('about', models.TextField()),
                ('his_photo', models.ImageField(height_field=100, upload_to=b'', width_field=100)),
                ('experience', models.IntegerField()),
            ],
        ),
    ]
