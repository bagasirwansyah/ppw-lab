from django.shortcuts import render

from lab_1.views import birth_date, mhs_name

bio_dict = [{'subject': 'Name', 'value': mhs_name},
            {'subject': 'Birth Date', 'value': birth_date.strftime('%d %B %Y')},
            {'subject': 'Sex', 'value': 'Male'}]


def index(request):
    response = {"bio_dict": bio_dict}
    return render(request, 'description_lab2addon.html', response)
