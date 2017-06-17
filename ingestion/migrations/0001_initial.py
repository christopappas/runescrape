# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 03:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('last_modified_time', models.DateTimeField(auto_now=True, db_index=True, verbose_name=b'last-modified')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ('-created_time',),
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('last_modified_time', models.DateTimeField(auto_now=True, db_index=True, verbose_name=b'last-modified')),
                ('skillname', models.CharField(choices=[(b'Overall', b'Overall'), (b'Attack', b'Attack'), (b'Defence', b'Defence'), (b'Strength', b'Strength'), (b'Hitpoints', b'Hitpoints'), (b'Ranged', b'Ranged'), (b'Prayer', b'Prayer'), (b'Magic', b'Magic'), (b'Cooking', b'Cooking'), (b'Woodcutting', b'Woodcutting'), (b'Fletching', b'Fletching'), (b'Fishing', b'Fishing'), (b'Firemaking', b'Firemaking'), (b'Crafting', b'Crafting'), (b'Smithing', b'Smithing'), (b'Mining', b'Mining'), (b'Herblore', b'Herblore'), (b'Agility', b'Agility'), (b'Thieving', b'Thieving'), (b'Slayer', b'Slayer'), (b'Runecraft', b'Runecraft'), (b'Hunter', b'Hunter')], max_length=255)),
                ('rank', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('level', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('xp', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='character',
            name='player_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingestion.Skill'),
        ),
    ]
