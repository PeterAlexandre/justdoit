from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from justdoit.todolist import choices


class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class ToDo(BaseModel):
    title = models.CharField(_('Title'), max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Owner'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Todolist')
        verbose_name_plural = _('Todolists')


class Task(BaseModel):
    STATUS = choices.TaskStatus

    title = models.CharField(_('Title'), max_length=60)
    description = models.TextField(_('Description'), blank=True)
    deadline = models.DateTimeField(_('Deadline'), blank=True, null=True)
    status = models.CharField(_('Status'), max_length=4, choices=STATUS.choices, default='OPEN')
    to_do = models.ForeignKey('ToDo', on_delete=models.CASCADE, related_name='tasks', related_query_name='task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')


def profile_picture(instance, filename):
    return f'profile/{instance.pk}.{filename.split(".")[-1]}'


class Profile(BaseModel):
    picture = models.ImageField(_('Picture'), upload_to=profile_picture, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username if self.user else _('Undefine profile')

    def save(self, *args, **kwargs):
        if self.pk:
            profile = Profile.objects.only('picture').get(pk=self.pk)
            if profile.picture:
                profile.picture.delete(False)
        super().save(*args, **kwargs)
