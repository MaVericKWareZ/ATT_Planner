from django.db import models

from att_planner.commons.models import CreatedModified
from att_planner.planner.models.bucket import Bucket


class Task(CreatedModified):

    class ProgressEnum(models.TextChoices):
        NOT_STARTED = 'NOT_STARTED', 'Task is not started'
        IN_PROGRESS = 'IN_PROGRESS', 'Task is in progress'
        COMPLETED = 'COMPLETED', 'Task is in progress'

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    progress = models.CharField(max_length=255, choices=ProgressEnum.choices, default=ProgressEnum.NOT_STARTED)
    priority = models.PositiveIntegerField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'({self.id}: {self.name}, {self.progress}, {self.description}, {self.priority},' \
               f' {self.start_date}, {self.end_date})'

    class Meta:
        db_table = 'task'
        app_label = 'planner'
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
