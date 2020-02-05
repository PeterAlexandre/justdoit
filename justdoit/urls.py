from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from justdoit.todolist.views import IndexView, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('todolist/', include('justdoit.todolist.urls')),
]
