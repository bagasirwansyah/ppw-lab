from django.urls import path

from lab_2.views import index

urlpatterns = [
    path('', index, name='index'),
]
