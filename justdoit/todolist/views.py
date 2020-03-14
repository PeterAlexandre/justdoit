from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DJLoginView
from django.views.generic import DetailView, ListView
from django.urls import reverse

from justdoit.todolist.models import ToDo
from justdoit.todolist.forms import TaskForm, TaskInlineFormSet


# Authentication views
class LoginView(DJLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = super().get_success_url()
        if self.request.path == url:
            return reverse('home')
        return url


# ToDo View
class ToDoDetailView(LoginRequiredMixin, DetailView):
    model = ToDo
    template_name = 'todolist/todo_detail.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            todo_list=self.queryset.exclude(pk=self.object.pk).order_by('-updated_at'),
            task_formset=TaskInlineFormSet(instance=self.object),
            task_form=TaskForm()
        )

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = super().get_queryset().filter(owner=self.request.user)
        return self.queryset


class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = 'index.html'
    context_object_name = 'todo_list'
    ordering = ['-updated_at']
