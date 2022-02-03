from datetime import datetime

import pytz
from django.shortcuts import redirect, render

from lab_3.models import Diary


def index(request):
    diary_dict = Diary.objects.all().values()
    return render(request, 'to_do_list.html', {'diary_dict': convert_queryset_into_json(diary_dict)})


def add_activity(request):
    if request.method == 'POST':
        try:
            date = datetime.strptime(request.POST['date'], '%Y-%m-%dT%H:%M')
            Diary.objects.create(date=date.replace(tzinfo=pytz.UTC), activity=request.POST['activity'])
            return redirect('/lab-3/')
        except:
            return redirect('/lab-3/')
    else:
        return redirect('/lab-3/')


def convert_queryset_into_json(queryset):
    ret_val = []
    for data in queryset:
        ret_val.append(data)
    return ret_val
