# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20171126_0153'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bestseller',
            options={'ordering': ('product',)},
        ),
    ]
