# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-21 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tookoda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='google_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=999)),
            ],
        ),
    ]
