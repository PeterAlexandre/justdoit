from django.contrib.auth.models import User
from django.db import models

from justdoit.todolist import choices


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ToDo(BaseModel):
    title = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Todolist'
        verbose_name_plural = 'Todolists'


class Task(BaseModel):
    STATUS = choices.TaskStatus

    title = models.CharField(max_length=60)
    description = models.TextField()
    deadline = models.DateTimeField(blank=True)
    status = models.CharField(max_length=4, choices=STATUS.choices, default='OPEN')
    to_do = models.ForeignKey('ToDo', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='tasks', related_query_name='task', verbose_name='Tags')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Tag(BaseModel):
    COLOR = choices.TagColor

    title = models.CharField(max_length=20)
    color = models.CharField(max_length=7, choices=COLOR.choices, default='GRA')
