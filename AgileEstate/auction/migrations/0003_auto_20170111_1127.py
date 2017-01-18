# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-11 11:27
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auto_20170104_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biddingmodel',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 11, 27, 13, 257011, tzinfo=utc), validators=[django.core.validators.MinValueValidator(models.DateTimeField(default=datetime.datetime(2017, 1, 11, 11, 27, 13, 256950, tzinfo=utc)))]),
        ),
        migrations.AlterField(
            model_name='biddingmodel',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 11, 27, 13, 256950, tzinfo=utc)),
        ),
    ]