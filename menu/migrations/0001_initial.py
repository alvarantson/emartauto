# Generated by Django 2.1.3 on 2019-11-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=99, unique=True)),
                ('price', models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='menu_lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(blank=True, max_length=999)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
