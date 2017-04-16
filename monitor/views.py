# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#from service.datacollector import f

def testview(request):
 #   print f()
    return HttpResponse("Hurra")



