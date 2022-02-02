from datetime import datetime

from django.shortcuts import render

mhs_name = 'Bagas Irwansyah'
curr_date = datetime.now()
birth_date = datetime(1998, 2, 12)
npm = 1606880730


def index(request):
    response = {'name': mhs_name, 'age': calculate_age(birth_date), 'npm': npm}
    return render(request, 'index_lab1.html', response)


def calculate_age(date_of_birth):
    age = ((curr_date - date_of_birth) / 365.25).days
    return age if age > 0 else 0
