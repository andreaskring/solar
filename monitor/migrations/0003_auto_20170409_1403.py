# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_panelstatus_apartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panelstatus',
            name='apartment',
            field=models.IntegerField(null=True),
        ),
    ]