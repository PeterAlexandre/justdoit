from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

from justdoit.api.v1.todolist import views

router = DefaultRouter()

# App: core
router.register('todo', views.ToDoViewSet, basename='todolist.todo')
router.register('task', views.TaskViewSet, basename='todolist.task')

schema_view = get_schema_view(
   openapi.Info(
      title="Justodoit API",
      default_version='v1',
      description="A generated API documentation to use Justdoit API.",
      contact=openapi.Contact(email="petermiguel99@gmail.com"),
   ),
)

app_name = 'v1'
urlpatterns = (
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
)
