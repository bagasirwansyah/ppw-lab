from django.urls import path

from lab_5.views import add_todo, delete_todo, index

urlpatterns = [
    path('', index, name='index'),
    path('add_todo/', add_todo, name='add_todo'),
    path('delete_todo/<int:pk_id>/', delete_todo, name='delete_todo')
]
