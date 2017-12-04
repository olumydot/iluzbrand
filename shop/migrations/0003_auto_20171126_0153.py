# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bestseller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='SKU',
            field=models.TextField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='bestseller',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured', to='shop.Product'),
        ),
    ]
