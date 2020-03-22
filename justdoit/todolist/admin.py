from django.contrib import admin

from justdoit.todolist.models import ToDo, Task

admin.site.register(ToDo)
admin.site.register(Task)
