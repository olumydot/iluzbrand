# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-03 05:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'email', 'verbose_name_plural': 'emails'},
        ),
    ]
