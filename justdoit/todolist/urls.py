from django.urls import path

from .views import BoardList, BoardDetail, Lists, ListDetail

urlpatterns = [
    path('', BoardList.as_view(), name='index'),
    path('board/<int:pk>', BoardDetail.as_view(), name='board'),
    path('list/', Lists.as_view(), name='lists'),
    path('list/<int:pk>', ListDetail.as_view(), name='list_detail')
]
