# Generated by Django 2.1.3 on 2019-11-02 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmstudio', '0006_auto_20191101_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmstudio_img',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
