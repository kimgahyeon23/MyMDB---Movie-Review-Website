# Generated by Django 2.0.5 on 2019-06-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20190622_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieimage',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]
