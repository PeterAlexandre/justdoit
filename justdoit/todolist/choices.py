from django.db.models import TextChoices


class TaskStatus(TextChoices):
    ARCHIVED = 'ARCH', 'Archived'
    DONE = 'DONE', 'Done'
    OPEN = 'OPEN', 'Open'


class TagColor(TextChoices):
    BLUE = 'BLU', '#0066ff'
    GRAY = 'GRA', '#6897bb'
    GREEN = 'GRE', '#70818D'
    ORANGE = 'ORA', '#ff8800'
    PURPLE = 'PUR', '#aa00ff'
    RED = 'RED', '#ff5733'
    YELLOW = 'YEL', '#fef65b'
