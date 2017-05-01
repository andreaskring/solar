# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import PanelStatus


# Create your views here.

# from service.datacollector import f

def testview(request):
    #   print f()
    return HttpResponse("Hurra")


def home(requests):
    pass


def downtime_form(request):
    panel_list = PanelStatus.objects.all()
    context = {'panel_list': panel_list}
    return render(request, 'monitor/downtime.html', context)


# def get_timedelta(request):
#     interval = request.POST['interval']
#     if interval == 'month':
#         return datetime.timedelta(days=30)
#     elif interval == 'week':
#         return datetime.timedelta(days=7)
#     elif interval == 'day':
#         return datetime.timedelta(days=1)
#     elif interval == 'hour':
#         return datetime.timedelta(hours=1)
#     else:
#         raise 'Interval exception'


def downtime_data(request):
    # Refactor into get_date function
    start_year, start_month, start_day = [int(x) for x in request.POST['startdate'].split('-')]
    end_year, end_month, end_day = [int(x) for x in request.POST['enddate'].split('-')]

    apartment = 11

    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)
    current_timestamp = start_date

    while current_timestamp < end_date:
        next_timestamp = current_timestamp + datetime.timedelta(hours=int(request.POST['interval']))
        count_all = PanelStatus.objects.filter(timestamp__gte=current_timestamp,
                                               timestamp__lt=next_timestamp,
                                               apartment=apartment,
                                               ).count()
        count_error = PanelStatus.objects.filter(timestamp__gte=current_timestamp,
                                                 timestamp__lt=next_timestamp,
                                                 apartment=apartment,
                                                 status='ERROR'
                                                 ).count()
        percentage = 100*float(count_error)/count_all

        current_timestamp = next_timestamp
    # return HttpResponse(request.POST['startdate'] + ' ' + request.POST['enddate'])
    return HttpResponse(100*float(count_error)/count_all)
