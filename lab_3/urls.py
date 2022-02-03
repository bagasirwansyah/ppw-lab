from django.urls import path

from lab_3.views import add_activity, index

urlpatterns = [
    path('', index, name='index'),
    path('add_activity/', add_activity, name='add_activity')
]
