# Generated by Django 3.1.7 on 2021-04-07 04:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0040_auto_20210406_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='slug',
        ),
        migrations.AlterField(
            model_name='orderitems',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 16, 2, 43, 550650)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 6, 16, 2, 43, 551613)),
        ),
    ]
