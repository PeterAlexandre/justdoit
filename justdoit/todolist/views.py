from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView as DJLoginView
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView
from django.views import View

from justdoit.todolist.models import ToDo, Profile
from justdoit.todolist.forms import TaskForm, TaskInlineFormSet, ProfileForm, UserCreationForm


# Authentication views
class LoginView(DJLoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        url = super().get_success_url()
        if self.request.path == url:
            return reverse('todolist:home')
        return url


class UserCreateView(CreateView):
    template_name = 'register.html'
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('todolist:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=form.instance)
        login(self.request, form.instance)
        return response


# ToDo View
class ToDoDetailView(LoginRequiredMixin, DetailView):
    model = ToDo
    template_name = 'todolist/todo_detail.html'
    context_object_name = 'todo'

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            todo_list=self.queryset.exclude(pk=self.object.pk).order_by('-updated_at'),
            task_formset=TaskInlineFormSet(
                instance=self.object,
                queryset=self.object.tasks.filter(status='OPEN').order_by('-updated_at')
            ),
            task_form=TaskForm(),
            completed_tasks=self.object.tasks.filter(status='DONE').order_by('-updated_at')
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

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = super().get_queryset().filter(owner=self.request.user)
        return self.queryset


class ProfileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.request.user.profile, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todolist:home'))
        return HttpResponseBadRequest()
