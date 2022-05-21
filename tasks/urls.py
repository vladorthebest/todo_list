from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('', views.TaskList.as_view(), name="list tasks"),

    path('update_task/<int:pk>/', views.TaskUpdate.as_view(), name="update task"),
    path('detail_task/<int:pk>/', views.TaskDetail.as_view(), name="detail task"),
    path('create_task/', views.TaskCreate.as_view(), name="create task"),
    path('delete_task/<int:pk>/', views.TaskDelete.as_view(), name="delete task"),

    path('register/', views.RegisterPage.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page= "login")),
]