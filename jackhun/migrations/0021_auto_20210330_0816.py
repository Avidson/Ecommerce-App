# Generated by Django 3.1.7 on 2021-03-30 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0020_auto_20210311_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 8, 16, 26, 856885)),
        ),
    ]
