# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import PanelStatus

# Create your views here.

#from service.datacollector import f

def testview(request):
 #   print f()
    return HttpResponse("Hurra")


def home(requests):
    pass


def hourly(request):
    panel_list = PanelStatus.objects.all()
    context = {'panel_list': panel_list}
    return render(request, 'monitor/hourly.html', context)

