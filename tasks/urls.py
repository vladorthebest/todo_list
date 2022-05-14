from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name="list tasks"),
    path('update_task/<int:pk>/', views.update_task, name="update task"),
    path('delete_task/<int:pk>/', views.delete_task, name="delete task"),
]