# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0169_auto_20170524_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
