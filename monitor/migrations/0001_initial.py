# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PanelStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp')),
                ('power', models.IntegerField(null=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Apartment')),
            ],
        ),
    ]
