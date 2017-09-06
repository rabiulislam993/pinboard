# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('done', models.BooleanField(default=False)),
                ('done_at', models.DateTimeField(blank=True, null=True)),
                ('starred', models.BooleanField(default=False)),
                ('priority', models.PositiveIntegerField(choices=[(1, b'Low'), (2, b'Medium'), (3, b'High')], default=1, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pin',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='pinboard.Tag'),
        ),
    ]