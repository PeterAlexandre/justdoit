from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DJLoginView
from django.views.generic import CreateView, DetailView, DeleteView, ListView, TemplateView, UpdateView
from django.urls import reverse, reverse_lazy

from justdoit.todolist.forms import ToDoForm
from justdoit.todolist.models import ToDo


# General views
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


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
class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    form_class = ToDoForm
    template_name = 'todolist/todo_create.html'

    def get_success_url(self):
        return reverse('todolist:todo_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    model = ToDo
    form_class = ToDoForm
    template_name = 'todolist/todo_update.html'

    def get_success_url(self):
        return reverse('todolist:todo_detail', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDo
    template_name = 'todolist/todo_delete.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todolist:home')


class ToDoDetailView(LoginRequiredMixin, DetailView):
    model = ToDo
    template_name = 'todolist/todo_detail.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        return super().get_context_data(todo_list=self.queryset.exclude(pk=self.object.pk).order_by('-updated_at'))

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = super().get_queryset().filter(owner=self.request.user)
        return self.queryset


class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDo
    template_name = 'index.html'
    context_object_name = 'todo_list'
