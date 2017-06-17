# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-13 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import ingestion.models


class Migration(migrations.Migration):

    dependencies = [
        ('ingestion', '0007_auto_20170510_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date-created'),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=ingestion.models.LowerCaseCharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'date-created'),
        ),
    ]
