# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-05 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0021_auto_20170104_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='private_message',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='chat.Profile'),
        ),
    ]
