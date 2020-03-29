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
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=4, choices=STATUS.choices, default='OPEN')
    to_do = models.ForeignKey('ToDo', on_delete=models.CASCADE, related_name='tasks', related_query_name='task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


def profile_picture(instance, filename):
    return f'profile/{instance.pk}.{filename.split(".")[-1]}'


class Profile(BaseModel):
    picture = models.ImageField(upload_to=profile_picture, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username if self.user else 'Undefine profile'

    def save(self, *args, **kwargs):
        if self.pk:
            print('test')
            profile = Profile.objects.only('picture').get(pk=self.pk)
            if profile.picture:
                profile.picture.delete(False)
        super().save(*args, **kwargs)
