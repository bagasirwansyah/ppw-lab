from django.urls import path

from lab_1.views import index

urlpatterns = [
    path('', index, name='index'),
]
