# Generated by Django 3.1 on 2021-03-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('michijapp', '0017_auto_20210211_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image5',
            field=models.FileField(default='upload Image', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='item',
            name='image6',
            field=models.FileField(default='upload Image', upload_to='images/'),
        ),
    ]
