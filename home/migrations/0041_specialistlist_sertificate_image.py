# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 02:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('home', '0040_specialistpage_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialistlist',
            name='sertificate_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image', verbose_name='Изображение сертификата'),
        ),
    ]
