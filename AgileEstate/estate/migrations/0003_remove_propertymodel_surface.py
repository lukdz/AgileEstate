# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-04 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_auto_20170104_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertymodel',
            name='surface',
        ),
    ]
