# Generated by Django 2.1.2 on 2018-10-25 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 10, 25, 23, 7, 35, 527268)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(),
        ),
    ]