# Generated by Django 2.1.3 on 2019-11-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmstudio', '0005_auto_20191101_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmstudio_lang',
            name='book',
            field=models.CharField(blank=True, max_length=999),
        ),
        migrations.AlterField(
            model_name='filmstudio_lang',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
