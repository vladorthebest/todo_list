from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from tasks.models import *
from tasks.forms import *


class TaskList(LoginRequiredMixin, ListView):
    #main page with all user's tasks

    model = Task
    context_object_name = 'tasks' #name context in html
    ordering = ['status']  #sorting by status

    def get_context_data(self, **kwargs):
        #function for get data from DataBase

        context = super().get_context_data(**kwargs)

        #save all user's tasks in context['tasks']
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        #how much user have tasks with status 'False'
        context['count'] = context['tasks'].filter(status=False).count()

        #search in tasks
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        #search_input for html form "search"
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('list tasks') #return user on "list tasks" page when he created task
    template_name = 'tasks/create_task.html'
    fields = ['title', 'description', 'status'] #create form have only these fields
    #for all fields we can use magic method '__all__'

    def form_valid(self, form):
        #def started if form valid
        form.instance.user = self.request.user
        #add user in new task

        return super(TaskCreate, self).form_valid(form)

    

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy('list tasks') #return user on "list tasks" page when he updated task
    template_name = 'tasks/create_task.html'
    fields = ['title', 'description', 'status'] #update form have only these fields

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('list tasks') #return user on "list tasks" page when he deleted task



class CustomLoginView(LoginView):
    template_name = 'tasks/login.html'
    fields = '__all__'
    redirect_authenticated_user = True #redirect if user authenticated 
    def get_success_url(self):
        return '/'


class RegisterPage(FormView):
    template_name = 'tasks/register.html'
    form_class = UserCreationForm #form for registration
    redirect_authenticated_user = True
    success_url = reverse_lazy('list tasks') #return user on "list tasks" page when he register

    def form_valid(self, form):
        #if form register valid
        user = form.save() #save new user
        if user is not None:
            login(self.request, user) #login new user
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            #if user authenticated - redirect on main page
            return redirect('/') 
        return super(RegisterPage, self).get(*args, **kwargs)


def tasktrue(request, pk):
    task = Task.objects.get(id=pk)
    task.status = not task.status
    task.save()
    return redirect('/')