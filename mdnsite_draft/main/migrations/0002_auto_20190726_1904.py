# Generated by Django 2.2.3 on 2019-07-26 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
    ]
