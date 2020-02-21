from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from justdoit.api.v1.todolist import serializers
from justdoit.todolist.models import ToDo, Task, Tag


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.order_by('-updated_at')
    serializer_class = serializers.ToDoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.order_by('created_at')
    serializer_class = serializers.TaskSerializer
    permission_classes = (IsAuthenticated,)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.order_by('pk')
    serializer_class = serializers.TagSerializer
    permission_classes = (IsAuthenticated,)
