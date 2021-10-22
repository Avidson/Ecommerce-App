# Generated by Django 3.1.5 on 2021-01-28 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='jackhun.items')),
            ],
        ),
    ]
