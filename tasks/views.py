from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

from tasks.models import *
from tasks.forms import *


class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/'

def tasks(request):
    tasks = Task.objects.all()[::-1]
    
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

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {'task': task}
    return render(request, 'tasks/delete.html', context)