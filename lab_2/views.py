from django.shortcuts import render

from lab_1.views import mhs_name

landing_page_content = 'I am a programmer that resides in Jakarta, Indonesia'


def index(request):
    response = {'name': mhs_name, 'content': landing_page_content}
    return render(request, 'index_lab2.html', response)
