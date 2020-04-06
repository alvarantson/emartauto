# Generated by Django 2.2.9 on 2020-04-06 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200406_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='kirjad_priority',
            field=models.CharField(choices=[('M', 'midagi'), ('V', 'vaatamine'), ('L', 'lisamine'), ('K', 'muutmine')], default='', max_length=999),
        ),
    ]
