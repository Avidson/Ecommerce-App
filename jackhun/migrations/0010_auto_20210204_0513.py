# Generated by Django 3.1.5 on 2021-02-04 13:13

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('jackhun', '0009_emailsubscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='leave_a_message',
            field=djrichtextfield.models.RichTextField(),
        ),
    ]
