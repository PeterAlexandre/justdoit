from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class TaskStatus(TextChoices):
    OPEN = 'OPEN', _('Open')
    DONE = 'DONE', _('Done')
