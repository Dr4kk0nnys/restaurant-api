# Generated by Django 3.1.3 on 2020-11-17 14:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201117_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinValueValidator('10')]),
        ),
    ]
