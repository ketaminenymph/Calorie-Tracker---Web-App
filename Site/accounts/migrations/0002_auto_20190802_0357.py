# Generated by Django 2.2.3 on 2019-08-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1),
        ),
    ]
