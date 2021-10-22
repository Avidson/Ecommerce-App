# Generated by Django 3.1.5 on 2021-02-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('michijapp', '0009_auto_20210201_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_contact', models.IntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(help_text='Enter a valid email address', max_length=254)),
                ('your_address', models.CharField(max_length=100)),
                ('leave_a_message', models.TextField(default='Type in you message here')),
            ],
        ),
    ]
