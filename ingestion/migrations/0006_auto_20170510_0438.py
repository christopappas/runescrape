# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingestion', '0005_auto_20170510_0433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skillname',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='skill',
            name='character',
            field=models.ForeignKey(db_column=b'character', default=b'', on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='ingestion.Character'),
        ),
    ]
