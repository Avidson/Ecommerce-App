# Generated by Django 3.1.5 on 2021-02-04 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('michijapp', '0012_auto_20210204_0514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
    ]
