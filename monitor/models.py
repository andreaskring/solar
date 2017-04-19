# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Apartment(models.Model):
    number = models.IntegerField(primary_key=True)
    panel_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return 'Apartment ' + str(self.number)


@python_2_unicode_compatible
class PanelStatus(models.Model):
    status = models.CharField(max_length=10)
    timestamp = models.DateTimeField('Timestamp')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    power = models.IntegerField(null=True)

    def __str__(self):
        return str(self.timestamp) + '     Apartment ' + str(self.apartment) + ' Power: ' + str(self.power)



