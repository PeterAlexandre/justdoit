from django.urls import path

from justdoit.todolist import views

app_name = 'todolist'
urlpatterns = [
    # ToDo URLs
    path('todo/<int:pk>/', views.ToDoDetailView.as_view(), name='todo_detail'),
    path('', views.ToDoListView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
