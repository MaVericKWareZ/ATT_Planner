from django.db import models

from att_planner.commons.models import CreatedModified


class Bucket(CreatedModified):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'({self.id}: {self.name}, {self.description})'

    class Meta:
        db_table = 'bucket'
        app_label = 'planner'
        verbose_name = 'bucket'
        verbose_name_plural = 'buckets'
