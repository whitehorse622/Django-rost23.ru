# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 15:42
from __future__ import unicode_literals

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_categoryprice_listprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='home.CategoryPrice'),
        ),
    ]
