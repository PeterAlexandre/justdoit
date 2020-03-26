from django.contrib import admin

from justdoit.todolist.models import ToDo, Task, Profile

admin.site.register(ToDo)
admin.site.register(Task)
admin.site.register(Profile)
