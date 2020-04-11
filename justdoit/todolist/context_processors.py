from justdoit.todolist.forms import ToDoForm, ProfileForm
from django.conf import settings


def todo_context(request):
    return {
        'todo_create': ToDoForm(request.user),
        'profile_create': ProfileForm(request.user),
        'allow_media': settings.ALLOW_MEDIA
    }
