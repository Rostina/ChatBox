# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-07 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20160929_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='title',
            field=models.CharField(blank=True, default='Post', max_length=125, null=True),
        ),
    ]
