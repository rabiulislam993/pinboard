# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import pinboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('pinboard', '0009_auto_20170905_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='style_transform_range',
            field=models.IntegerField(blank=True, default=pinboard.models.get_range),
        ),
    ]
