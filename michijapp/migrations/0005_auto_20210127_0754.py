# Generated by Django 3.1.5 on 2021-01-27 15:54

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('michijapp', '0004_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.FileField(default='Upload Image', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=djrichtextfield.models.RichTextField(),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to='images'),
        ),
    ]
