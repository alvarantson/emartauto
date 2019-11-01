# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-25 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50, unique=True)),
                ('Gmaps_x', models.CharField(max_length=10, unique=True)),
                ('Gmaps_y', models.CharField(max_length=10, unique=True)),
                ('Gmaps_zoom', models.CharField(max_length=2, unique=True)),
                ('Gmaps_API', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='langs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=3, unique=True)),
                ('flag', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='navbar_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=3, unique=True)),
                ('index', models.CharField(blank=True, max_length=15)),
                ('about', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
