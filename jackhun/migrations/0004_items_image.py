# Generated by Django 3.1.5 on 2021-01-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0003_auto_20210129_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='image',
            field=models.FileField(default='Upload Image', upload_to='images/'),
        ),
    ]