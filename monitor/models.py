# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

#@python_2_unicode_compatible

class PanelStatus(models.Model):
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField('Timestamp')
    apartment = models.IntegerField(null=True)
    power = models.IntegerField(null=True)


