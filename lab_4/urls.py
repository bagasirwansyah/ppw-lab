from django.urls import path

from lab_4.views import index, message_post, message_table

urlpatterns = [
    path('', index, name='index'),
    path('add_message/', message_post, name='add_message'),
    path('result_table/', message_table, name='result_table'),
]