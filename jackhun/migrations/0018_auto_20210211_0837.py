# Generated by Django 3.1.5 on 2021-02-11 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0017_auto_20210209_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 8, 37, 55, 503108)),
        ),
    ]
