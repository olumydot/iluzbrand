# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-28 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='Black', max_length=40),
            preserve_default=False,
        ),
    ]
