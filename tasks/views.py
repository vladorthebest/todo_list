from django.shortcuts import render, redirect

from tasks.models import *
from tasks.forms import *

def tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form }
    return render(request, 'tasks/tasks.html', context)  
   

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'task': task, 'form': form}
    return render(request, 'tasks/update_task.html', context)
