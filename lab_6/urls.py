from django.urls import path

from lab_6.views import index

urlpatterns = [
    path('', index, name='index'),
]
