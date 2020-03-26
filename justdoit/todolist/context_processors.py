from justdoit.todolist.forms import ToDoForm, ProfileForm


def todo_context(request):
    return {
        'todo_create': ToDoForm(request.user),
        'profile_picture': ProfileForm(request.user)
    }
