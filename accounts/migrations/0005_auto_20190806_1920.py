# Generated by Django 2.2.3 on 2019-08-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190806_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date Of Birth(YYYY-MM-DD)'),
        ),
    ]
