# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-07 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buildings', '0008_auto_20180606_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holes',
            name='sensorId',
            field=models.IntegerField(default=0, verbose_name='传感器编号'),
        ),
    ]
