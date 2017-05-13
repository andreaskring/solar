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
    return render(request, 'monitor/downtime-form.html', context)


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

    start_date = datetime.datetime(start_year, start_month, start_day, 0, 0, 0)
    end_date = datetime.datetime(end_year, end_month, end_day, 0, 0, 0)
    current_timestamp = start_date

    data = []
    while current_timestamp < end_date:
        # next_timestamp = current_timestamp + datetime.timedelta(hours=int(request.POST['interval']))
        next_timestamp = current_timestamp + datetime.timedelta(hours=1)
        count_all = PanelStatus.objects.filter(timestamp__gte=current_timestamp,
                                               timestamp__lt=next_timestamp,
                                               apartment=apartment,
                                               ).count()
        count_error = PanelStatus.objects.filter(timestamp__gte=current_timestamp,
                                                 timestamp__lt=next_timestamp,
                                                 apartment=apartment,
                                                 status='ERROR'
                                                 ).count()
        if not count_all == 0:
            percentage = 100 * float(count_error) / count_all
        else:
            percentage = 'Ingen data'
        timestamp_percentage = {'starttime': current_timestamp.isoformat(),
                                'endtime': next_timestamp.isoformat(),
                                'percentage': percentage}
        data.append(timestamp_percentage)

        current_timestamp = next_timestamp

    context = {'timestamp_percentage': data}
    # return HttpResponse(request.POST['startdate'] + ' ' + request.POST['enddate'])
    return render(request, 'monitor/downtime-data.html', context)
