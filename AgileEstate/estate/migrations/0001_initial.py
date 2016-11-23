# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('country', models.TextField(verbose_name=[('FR', 'France'), ('JP', 'Japan'), ('GB', 'United Kingdom'), ('CA', 'Canada'), ('DE', 'Germany'), ('PL', 'Poland'), ('CH', 'Switzerland'), ('HK', 'Hong Kong'), ('US', 'United States of America')])),
                ('city', models.TextField(verbose_name=[('WRO', 'Wroclaw'), ('ZUR', 'Zurich'), ('NYK', 'New York'), ('PAR', 'Paris'), ('MTL', 'Montreal'), ('BER', 'Berlin'), ('TOK', 'Tokio'), ('WDC', 'Washington DC'), ('LON', 'London')])),
                ('surface', models.DecimalField(max_digits=1002, validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2)),
                ('num_rooms', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(3)])),
                ('minimal_price', models.DecimalField(max_digits=1002, default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2)),
                ('actual_price', models.DecimalField(max_digits=1002, default=models.DecimalField(max_digits=1002, default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2), validators=[django.core.validators.MinValueValidator(models.DecimalField(max_digits=1002, default=0.0, validators=[django.core.validators.MinValueValidator(0.0)], decimal_places=2))], decimal_places=2)),
            ],
        ),
    ]
