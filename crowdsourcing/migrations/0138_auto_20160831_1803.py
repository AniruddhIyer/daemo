# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-31 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdsourcing', '0137_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchgroup',
            name='hash',
            field=models.CharField(db_index=True, default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchgroup',
            name='rerun_key',
            field=models.CharField(db_index=True, max_length=64, null=True),
        ),
        migrations.AlterIndexTogether(
            name='matchgroup',
            index_together=set([('rerun_key', 'hash')]),
        ),
    ]
