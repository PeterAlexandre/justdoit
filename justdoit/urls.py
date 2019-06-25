from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('justdoit/', include('justdoit.todolist.urls')),
    path('admin/', admin.site.urls),
]
