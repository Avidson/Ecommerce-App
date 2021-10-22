# Generated by Django 3.1.7 on 2021-03-31 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0025_auto_20210331_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='seller_address',
            field=models.CharField(default='seller address', max_length=300),
        ),
        migrations.AddField(
            model_name='items',
            name='seller_name',
            field=models.CharField(default='seller name', max_length=100),
        ),
        migrations.AddField(
            model_name='items',
            name='seller_profile',
            field=models.TextField(default=False, help_text='Details of your company'),
        ),
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('Vehicle', 'Vehicle'), ('Electronics', 'Electronics'), ('Mobile Device', 'Mobile Device'), ('Computer Device', 'Computer Device'), ('Home Equipment', 'Home Equipment'), ('Fashion', 'Fashion'), ('Doors', 'Doors'), ('Doors Accessories', 'Doors Accessories')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 7, 4, 33, 532541)),
        ),
    ]
