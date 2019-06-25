from django.contrib import admin

from .models import Board, ColumnList, Task

admin.site.register(Board)
admin.site.register(ColumnList)
admin.site.register(Task)
