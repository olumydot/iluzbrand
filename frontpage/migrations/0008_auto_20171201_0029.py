# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-01 05:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0007_auto_20171130_2325'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blogpost',
        ),
        migrations.DeleteModel(
            name='Carousel',
        ),
    ]
