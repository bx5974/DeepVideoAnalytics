# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 23:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0004_auto_20170430_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tevent',
            name='event_type',
            field=models.CharField(choices=[('V', 'Video'), ('SE', 'S3 export'), ('SI', 'S3 import'), ('CL', 'Clustering'), ('E', 'Export as file')], default='V', max_length=2),
        ),
    ]
