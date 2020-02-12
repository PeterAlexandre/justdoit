from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from justdoit.todolist.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todolist/', include('justdoit.todolist.urls')),
]
