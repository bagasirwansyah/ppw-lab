from django.urls import path

from lab_3.views import index, add_activity

urlpatterns = [
    path('', index, name='index'),
    path('add_activity/', add_activity, name='add_activity')
]
