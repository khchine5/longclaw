# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-12 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('longclawsettings', '0002_auto_20170212_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='longclawsettings',
            name='currency_html_code',
            field=models.CharField(default='&pound;', max_length=12),
        ),
    ]
