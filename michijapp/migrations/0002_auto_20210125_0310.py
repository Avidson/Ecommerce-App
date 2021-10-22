# Generated by Django 3.1.5 on 2021-01-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('michijapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Security Door'), ('SP', 'Window'), ('OW', 'Door Accessories')], max_length=2),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('N', 'New'), ('FU', 'Second Hand'), ('BS', 'Best Seller')], max_length=2),
        ),
    ]
