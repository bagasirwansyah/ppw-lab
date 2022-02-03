from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from lab_5.forms import TodoForm
from lab_5.models import Todo

response = {}


def index(request):
    todo = Todo.objects.all()
    response['author'] = "Bagas"
    response['todo'] = todo
    response['todo_form'] = TodoForm
    html = 'lab_5/lab_5.html'
    return render(request, html, response)


def add_todo(request):
    form = TodoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        response['title'] = request.POST['title']
        response['description'] = request.POST['description']
        todo = Todo(title=response['title'], description=response['description'])
        todo.save()
        messages.success(request, "Successfully added Todo")
        return HttpResponseRedirect('/lab-5/')
    else:
        return HttpResponseRedirect('/lab-5/')


def delete_todo(request, pk_id):
    try:
        Todo.objects.get(id=pk_id).delete()
        messages.success(request, "Successfully remove Todo")
        return HttpResponseRedirect('/lab-5/')
    except:
        return HttpResponseRedirect('/lab-5/')
