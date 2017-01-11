# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-04 12:32
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biddingmodel',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 12, 32, 17, 331893, tzinfo=utc), validators=[django.core.validators.MinValueValidator(models.DateTimeField(default=datetime.datetime(2017, 1, 4, 12, 32, 17, 331833, tzinfo=utc)))]),
        ),
        migrations.AlterField(
            model_name='biddingmodel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 12, 32, 17, 331833, tzinfo=utc)),
        ),
    ]
