from django.urls import path, include

from justdoit.api.v1 import urls as urls_v1

app_name = 'api'
urlpatterns = (
    path('v1/', include(urls_v1)),
)
