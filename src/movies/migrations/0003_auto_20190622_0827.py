# Generated by Django 2.0.5 on 2019-06-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190622_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieimage',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d'),
        ),
    ]
