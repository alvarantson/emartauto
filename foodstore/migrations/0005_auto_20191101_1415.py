# Generated by Django 2.1.3 on 2019-11-01 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstore', '0004_auto_20191101_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodstore_lang',
            old_name='description',
            new_name='text',
        ),
    ]
