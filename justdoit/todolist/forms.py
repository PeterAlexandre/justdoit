from django.forms import ModelForm

from justdoit.todolist.models import ToDo, Task, Tag


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.owner = user

    def save(self, commit=True):
        if not self.instance.pk:
            self.instance.owner = self.owner
        return super().save(commit)


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['title']
