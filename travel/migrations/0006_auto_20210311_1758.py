# Generated by Django 3.1.7 on 2021-03-11 12:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_flights_dep_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='dep_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='flights',
            name='dep_date',
            field=models.DateField(default=datetime.date(2021, 3, 11)),
        ),
    ]