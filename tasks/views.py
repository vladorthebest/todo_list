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
   

