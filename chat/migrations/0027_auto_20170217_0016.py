# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-17 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0026_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendmessage',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
