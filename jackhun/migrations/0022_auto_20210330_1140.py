# Generated by Django 3.1.7 on 2021-03-30 23:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0021_auto_20210330_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 11, 40, 41, 456074)),
        ),
    ]
