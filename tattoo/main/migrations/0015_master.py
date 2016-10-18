# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_master'),
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
                ('his_photo', models.FileField(blank=True, null=True, upload_to=b'')),
                ('experience', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('link_on_works', models.TextField()),
            ],
        ),
    ]