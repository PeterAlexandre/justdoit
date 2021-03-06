from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.conf.urls.static import static

from justdoit.todolist.views import LoginView, UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('justdoit.api.urls')),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('justdoit.todolist.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
