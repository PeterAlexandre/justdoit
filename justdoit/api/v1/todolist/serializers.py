from rest_framework.serializers import ModelSerializer

from justdoit.todolist.models import ToDo, Task, Tag


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['pk', 'title']


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['pk', 'title', 'description', 'deadline', 'status', 'to_do', 'tags']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['pk', 'title', 'color']
