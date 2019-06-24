from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    title = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Board(BaseModel):

    users = models.ForeignKey(User, on_delete=models.CASCADE)
    lists = models.ForeignKey('List', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'boards'


class List(BaseModel):

    tasks = models.ForeignKey('Task', on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'list'
        verbose_name_plural = 'lists'


class Task(BaseModel):

    ACTIVE = 'ACTIVE'
    ARCHIVED = 'ARCHIVED'
    DONE = 'DONE'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (ARCHIVED, 'Archived'),
        (DONE, 'Done'),
    ]

    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default=ACTIVE)
    position = position = models.PositiveIntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
