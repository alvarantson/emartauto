# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-04-05 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0020_auto_20191103_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='toode',
            name='toode_id',
            field=models.CharField(default=b'', max_length=999),
        ),
    ]
