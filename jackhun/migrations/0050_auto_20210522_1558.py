# Generated by Django 3.1 on 2021-05-22 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0049_auto_20210522_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='label',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='orders',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 22, 15, 58, 46, 629802)),
        ),
    ]