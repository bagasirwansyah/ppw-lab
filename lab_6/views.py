from django.shortcuts import render


def index(request):
    return render(request, 'lab_6/lab_6.html')