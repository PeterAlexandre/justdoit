from django.urls import path, include
from rest_framework.routers import DefaultRouter

from justdoit.api.v1.todolist import views

router = DefaultRouter()

# App: core
router.register('todo', views.ToDoViewSet, basename='todolist.todo')
router.register('task', views.TaskViewSet, basename='todolist.task')

app_name = 'v1'
urlpatterns = (
    path('', include(router.urls)),
)
