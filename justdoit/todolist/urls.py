from django.urls import path

from justdoit.todolist import views

app_name = 'todolist'
urlpatterns = [
    # ToDo URLs
    path('todo/create/', views.ToDoCreateView.as_view(), name='todo_create'),
    path('todo/<int:pk>/update/', views.ToDoUpdateView.as_view(), name='todo_update'),
    path('todo/<int:pk>/delete/', views.ToDoDeleteView.as_view(), name='todo_delete'),
    path('todo/<int:pk>/', views.ToDoDetailView.as_view(), name='todo_detail'),
    path('', views.ToDoListView.as_view(), name='home'),
]
