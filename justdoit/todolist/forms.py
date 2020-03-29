from django import forms

from justdoit.todolist.models import ToDo, Task, Profile


class ToDoForm(forms.ModelForm):
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


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'status']


TaskInlineFormSet = forms.inlineformset_factory(
    ToDo,
    Task,
    fields=TaskForm.Meta.fields,
    extra=0
)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture']
