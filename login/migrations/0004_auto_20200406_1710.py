# Generated by Django 2.2.9 on 2020-04-06 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181119_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='kalender2_priority',
            field=models.CharField(choices=[('M', 'midagi'), ('V', 'vaatamine'), ('L', 'lisamine'), ('K', 'muutmine')], default='', max_length=999),
        ),
        migrations.AddField(
            model_name='worker',
            name='tooted_priority',
            field=models.CharField(choices=[('M', 'midagi'), ('V', 'vaatamine'), ('L', 'lisamine'), ('K', 'muutmine')], default='', max_length=999),
        ),
    ]
