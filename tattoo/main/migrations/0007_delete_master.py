# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 18:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Master',
        ),
    ]