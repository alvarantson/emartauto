# Generated by Django 2.1.3 on 2018-12-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20181230_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='index_lang',
            name='uuri_lahemalt',
            field=models.CharField(default='', max_length=99999),
        ),
        migrations.AlterField(
            model_name='index_lang',
            name='h2',
            field=models.CharField(default='', max_length=99999),
        ),
    ]
