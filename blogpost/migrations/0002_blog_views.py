# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
