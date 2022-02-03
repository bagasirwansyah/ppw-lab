from django.urls import path

from lab_2_addon.views import index

urlpatterns = [
    path('', index, name='index'),
]
