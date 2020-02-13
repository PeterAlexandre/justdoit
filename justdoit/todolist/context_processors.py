from justdoit.todolist.forms import ToDoForm


def todo_context(request):
    return {'todo_create': ToDoForm(request.user)}
