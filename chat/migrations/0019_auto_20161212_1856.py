# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-12 23:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0018_auto_20161212_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='user',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='chat.Profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chat',
            name='users',
            field=models.ManyToManyField(null=True, related_name='users', to='chat.Profile'),
        ),
    ]
