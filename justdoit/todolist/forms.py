from django.forms import ModelForm

from justdoit.todolist.models import ToDo, Task, Tag


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
