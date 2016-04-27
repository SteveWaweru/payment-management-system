# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 00:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20160426_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='expiry_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='installation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_chasis_number',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_registration_number',
            field=models.CharField(default=datetime.datetime(2016, 4, 27, 0, 42, 51, 212326, tzinfo=utc), max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
