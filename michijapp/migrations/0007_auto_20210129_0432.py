# Generated by Django 3.1.5 on 2021-01-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('michijapp', '0006_auto_20210129_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to='images/'),
        ),
    ]
