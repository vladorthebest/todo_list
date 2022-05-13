from django.shortcuts import render
from tasks.models import *

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})  
   

