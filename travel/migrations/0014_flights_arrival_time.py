# Generated by Django 3.1.7 on 2021-03-13 18:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_auto_20210314_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='arrival_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]