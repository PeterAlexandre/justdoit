from django.urls import path

from .views import BoardList, BoardDetail, ColumnLists

urlpatterns = [
    path('', BoardList.as_view(), name='index'),
    path('board/<int:pk>', BoardDetail.as_view(), name='board'),
    path('list/', ColumnLists.as_view(), name='lists'),
]
