from django.db.models import TextChoices


class TaskStatus(TextChoices):
    OPEN = 'OPEN', 'Open'
    DONE = 'DONE', 'Done'
